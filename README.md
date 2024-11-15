#Descrição

Este projeto implementa uma API RESTful para notificação automatizada de tickets gerados no Freshdesk, integrando-se ao Slack para envio de mensagens personalizadas. 

A solução inclui recursos como:

- Polling periódico na API do Freshdesk para identificação de novos tickets.
- Notificações automáticas enviadas ao Slack com informações como tipo de ticket, prioridade, grupo responsável e link direto para o ticket.
- Persistência de logs detalhados e configurações dinâmicas no MongoDB.
- Arquitetura modular com escalabilidade e flexibilidade para integrações futuras.

#Funcionalidades
- Integração com o Freshdesk para consulta de tickets via API REST.
- Personalização de notificações no Slack, incluindo emojis de prioridade e links para os tickets.
- Registro de logs no MongoDB, incluindo status de sucesso ou falha das notificações.
- Configuração dinâmica de parâmetros operacionais (ex.: tokens, URLs, frequência de polling) diretamente no MongoDB.
- Suporte para execução local ou em ambientes de nuvem, como AWS ou Azure.

#Tecnologias Utilizadas
- Linguagem de Programação: Python 3.8+
- Frameworks e Bibliotecas: Flask, APScheduler, Requests, PyMongo
- Banco de Dados: MongoDB
- Ferramentas Complementares: Slack Webhooks, Freshdesk API
