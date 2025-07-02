# Azure Databricks Incident Monitor and Auto Responder

Monitor Azure Databricks jobs using the REST API, log incidents to a file (simulating ServiceNow/Jira), and auto-respond to failures using a simple alerting script.

## Features
- Connects to Databricks API
- Logs job failures
- Simulates support ticket generation and response

## Technologies
- Python
- Azure Databricks REST API
- dotenv
- Logging

## Setup Instructions
1. Clone the repo
2. Add `.env` file with your token and host URL
3. Install requirements
4. Run `python main.py`
