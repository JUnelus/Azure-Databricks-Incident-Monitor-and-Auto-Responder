import datetime
import os

LOG_FILE = "logs/incident_log.txt"

def log_incident(job_name, job_id, status):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as file:
        timestamp = datetime.datetime.now().isoformat()
        file.write(f"{timestamp} | Job: {job_name} (ID: {job_id}) | Status: {status}\n")
