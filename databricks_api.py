import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DatabricksAPI:
    def __init__(self):
        self.host = os.getenv("DATABRICKS_HOST")
        self.token = os.getenv("DATABRICKS_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def list_jobs(self):
        url = f"{self.host}/api/2.1/jobs/list"
        response = requests.get(url, headers=self.headers)
        return response.json().get('jobs', [])

    def get_job_status(self, job_id):
        url = f"{self.host}/api/2.1/jobs/runs/list?job_id={job_id}&limit=1"
        response = requests.get(url, headers=self.headers)
        runs = response.json().get('runs', [])
        if runs:
            return runs[0]['state']['result_state']
        return "UNKNOWN"
