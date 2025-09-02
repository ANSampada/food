from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import UnknownJob

def get_jenkins():
    return Jenkins("http://localhost:8080", username="admin", password="admin")

def update_job(job_spec):
    jenkins = get_jenkins()
    try:
        job = jenkins[job_spec.name]
        job.update_config(job_spec.config)
        print(f"Updated Job: {job_spec.name}")
    except UnknownJob:
        jenkins.create_job(job_spec.name, job_spec.config)
        print(f"Created Job: {job_spec.name}")
