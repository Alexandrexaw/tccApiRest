## TCC - API RESTful

Este projeto aborda o desenvolvimento de uma API para notificação automatizada de tickets em sistemas de suporte. 
O objetivo geral foi criar um sistema integrado ao Freshdesk e Slack, permitindo notificações em tempo real sobre novos tickets, incluindo informações detalhadas,
como prioridade e link para consulta. 

### Metodologia e tecnologias envolvidas

Utilizou-se uma metodologia incremental, com foco em etapas de configuração, implementação e testes. 
O desenvolvimento empregou tecnologias como Flask, MongoDB e APScheduler, garantindo escalabilidade e persistência de dados. 

### Funcionalidades

- Integração com o Freshdesk para consulta de tickets via API REST.
- Personalização de notificações no Slack, incluindo emojis de prioridade e links para os tickets.
- Registro de logs no MongoDB, incluindo status de sucesso ou falha das notificações.
- Configuração dinâmica de parâmetros operacionais (ex.: tokens, URLs, frequência de polling) diretamente no MongoDB.
- Suporte para execução local ou em ambientes de nuvem, como AWS ou Azure.

### Requisitos de Implantação 

- Linguagem de Programação: Python 3.8+
- Frameworks e Bibliotecas: Flask, APScheduler, Requests, PyMongo
- Banco de Dados: MongoDB
- Ferramentas Complementares: Slack Webhooks, Freshdesk API
