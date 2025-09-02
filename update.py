from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import UnknownJob

def get_jenkins():
    return Jenkins("http://10.209.132.115:8080", username="sampada", password="11e16ad45ee52ec04022655004741c614f")

def update_job(job_spec):
    jenkins = get_jenkins()
    try:
        job = jenkins[job_spec.name]
        job.update_config(job_spec.config)
        print(f"Updated Job: {job_spec.name}")
    except UnknownJob:
        jenkins.create_job(job_spec.name, job_spec.config)
        print(f"Created Job: {job_spec.name}")
