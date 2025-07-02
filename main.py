from databricks_api import DatabricksAPI
from incident_logger import log_incident
from responder import auto_respond


def main():
    db = DatabricksAPI()
    jobs = db.list_jobs()

    for job in jobs:
        job_id = job['job_id']
        job_name = job['settings']['name']
        status = db.get_job_status(job_id)

        if status != 'SUCCESS':
            message = f"[ALERT] Job '{job_name}' (ID: {job_id}) failed with status: {status}"
            print(message)
            log_incident(job_name, job_id, status)
            auto_respond(job_id)


if __name__ == "__main__":
    main()
