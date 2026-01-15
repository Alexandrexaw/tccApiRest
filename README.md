![Language](https://img.shields.io/badge/Language-English-blue)

# Capstone Project - RESTful API

This project covers the development of an API for the automated notification of tickets in support systems. 
The general objective was to create a system integrated with Freshdesk and Slack, allowing real-time notifications about new tickets, including detailed information such as priority and a direct link for consultation.

## Methodology and Technologies
An incremental methodology was utilized, focusing on configuration, implementation, and testing phases. The development employed technologies such as Flask, MongoDB, and APScheduler, ensuring scalability and data persistence.

## Features

- **Freshdesk Integration:** Ticket retrieval via REST API.

- **Slack Customization:** Personalized notifications including priority-based emojis and direct ticket links.

- **Logging:** Record-keeping in MongoDB, including success or failure status of notifications.

- **Dynamic Configuration:** Operational parameters (e.g., tokens, URLs, polling frequency) managed directly within MongoDB.

- **Deployment Support:** Compatible with local execution or cloud environments such as AWS or Azure.

## Deployment Requirements

- **Programming Language:** Python 3.8+

- **Frameworks and Libraries:** Flask, APScheduler, Requests, PyMongo

- **Database:** MongoDB

- **Complementary Tools:** Slack Webhooks, Freshdesk API
***

![Português](https://img.shields.io/badge/Idioma-Portugu%C3%AAs-green)

# TCC - API RESTful

Este projeto aborda o desenvolvimento de uma API para notificação automatizada de tickets em sistemas de suporte. 
O objetivo geral foi criar um sistema integrado ao Freshdesk e Slack, permitindo notificações em tempo real sobre novos tickets, incluindo informações detalhadas,
como prioridade e link para consulta. 

## Metodologia e tecnologias envolvidas

Utilizou-se uma metodologia incremental, com foco em etapas de configuração, implementação e testes. 
O desenvolvimento empregou tecnologias como Flask, MongoDB e APScheduler, garantindo escalabilidade e persistência de dados. 

## Funcionalidades

- **Integração com o Freshdesk:** Consulta de tickets via API REST.
- **Personalização de notificações:**  Formatação para envio no Slack, incluindo emojis de prioridade e links para os tickets.
- **Registro de logs:** Através do MongoDB, foi sensibilizado status de sucesso ou falha das notificações.
- **Configuração:**  Parâmetros operacionais (ex.: tokens, URLs, frequência de polling) diretamente no MongoDB.
- **Suporte para execução:** Ambiento local ou em ambiente de nuvem, como AWS ou Azure.

## Requisitos de Implantação 

- **Linguagem de Programação:** Python 3.8+
- **Frameworks e Bibliotecas:** Flask, APScheduler, Requests, PyMongo
- **Banco de Dados:** MongoDB
- **Ferramentas Complementares:** Slack Webhooks, Freshdesk API
