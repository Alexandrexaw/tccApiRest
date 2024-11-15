import requests
from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
from datetime import datetime
import base64
import json

app = Flask(__name__)

# Configuração do MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client['ticket_logs']
logs_collection = db['logs']
config_collection = db['config']

#Mapeamentos
PRIORITY_MAP = {
    1: "Baixo ⚪",
    2: "Médio 🟡",
    3: "Alto 🟠",
    4: "Urgente 🔴"
}

GROUP_MAP = {
    156000206903: "Billing",
    156000206904: "Escalation",
    156000206907: "Customer Support"
}

# Importar chaves e dados sensiveis cadastrados no MongoDB
def get_config():
    config = config_collection.find_one()
    return {
        "FRESHDESK_URL": config.get("FRESHDESK_URL"),
        "API_TOKEN": config.get("API_TOKEN"),
        "SLACK_WEBHOOK_URL": config.get("SLACK_WEBHOOK_URL"),
        "FRESHDESK_TICKET_URL": config.get("FRESHDESK_TICKET_URL"),
        "polling_interval": config.get("polling_interval", 60)
    }
# Inicializar Configuração Padrão
def init_mongo():
    if config_collection.count_documents({}) == 0:
        config_collection.insert_one({
            "FRESHDESK_URL": "https://testeti.freshdesk.com/api/v2/tickets",
            "API_TOKEN": "XXXXXXXX",
            "SLACK_WEBHOOK_URL": "https://hooks.slack.com/services/",
            "FRESHDESK_TICKET_URL": "https://testeti.freshdesk.com/a/tickets/",
            "polling_interval": 60
        })
# Verificar novos tickets
LAST_TICKET_ID = None

#Polling e integração
def check_new_tickets():
    global LAST_TICKET_ID
    config = get_config()
    headers = {
        "Authorization": f"Basic {base64.b64encode((config['API_TOKEN'] + ':X').encode()).decode()}"
    }
    response = requests.get(config['FRESHDESK_URL'], headers=headers)
    if response.status_code == 200:
        tickets = response.json()
        if tickets:
            latest_ticket = tickets[0]
            if LAST_TICKET_ID is None or latest_ticket['id'] != LAST_TICKET_ID:
                LAST_TICKET_ID = latest_ticket['id']
                log_ticket(latest_ticket)
                send_slack_notification(latest_ticket)
    else:
        print(f"Erro ao consultar tickets: {response.status_code}")

# Funções de Log e Configuração
def log_ticket(ticket):
    logs_collection.insert_one({
        "ticket_id": ticket['id'],
        "subject": ticket['subject'],
        "notified_at": datetime.utcnow(),
        "status": "Processed"
    })

# Registra status do envio feito pela API no Mongo
def log_slack_status(ticket_id, success, error_message=None):
    logs_collection.insert_one({
        "ticket_id": ticket_id,
        "notified_at": datetime.utcnow(),
        "status": "Success" if success else "Failed",
        "error_message": error_message
    })


def get_polling_interval():
    config = get_config()
    return config['polling_interval']


# Enviar Notificação para Slack
def send_slack_notification(ticket):
    config = get_config()
    try:
        ticket_type = ticket.get("type", "N/A")
        created_at = ticket.get("created_at", "N/A")
        priority = PRIORITY_MAP.get(ticket.get("priority"), "N/A")
        group_id = ticket.get("group_id", "N/A")
        group_name = GROUP_MAP.get(group_id, "Desconhecido")
        subject = ticket.get("subject", "Sem Assunto")
        ticket_id = ticket.get("id")
        ticket_url = f"{config['FRESHDESK_TICKET_URL']}{ticket_id}"

        message = {
            "text": (
                f"*Novo Ticket Detectado!*\n\n"
                f"*Tipo de Ticket:* {ticket_type}\n"
                f"*Data/Hora de Criação:* {created_at}\n"
                f"*Prioridade:* {priority}\n"
                f"*Grupo de Suporte:* {group_name}\n"
                f"*Assunto:* {subject}\n"
                f"*Link do Ticket:* <{ticket_url}|Clique aqui para ver o ticket>"
            )
        }

        response = requests.post(
            config['SLACK_WEBHOOK_URL'],
            data=json.dumps(message),
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            log_slack_status(ticket_id, success=True)
        else:
            log_slack_status(ticket_id, success=False, error_message=response.text)
    except Exception as e:
        log_slack_status(ticket.get("id"), success=False, error_message=str(e))


# Endpoints
@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(logs_collection.find({}, {"_id": 0}))
    return jsonify({"logs": logs})


@app.route('/config', methods=['POST'])
def update_config():
    data = request.json
    config_collection.update_one({}, {"$set": data})
    scheduler.reschedule_job("polling_job", trigger="interval", seconds=data.get("polling_interval", 60))
    return jsonify({"message": "Configuração atualizada", "config": data})


# Inicializar banco e scheduler
init_mongo()
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_new_tickets, trigger="interval", seconds=get_polling_interval(), id="polling_job")
scheduler.start()

# Finalizar scheduler no encerramento
import atexit

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(port=5000)
