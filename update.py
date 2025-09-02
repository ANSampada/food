from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import UnknownJob

# Folder XML definition
FOLDER_XML = """<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder">
  <description>Recipes folder</description>
</com.cloudbees.hudson.plugins.folder.Folder>"""

def get_jenkins():
    return Jenkins("http://10.209.132.115:8080", username="sampada", password="11e16ad45ee52ec04022655004741c614f")

def ensure_folder(jenkins, folder_name):
    """Create Jenkins folder if it doesn't exist"""
    if folder_name not in jenkins.keys():
        jenkins.create_job(folder_name, FOLDER_XML)
        print(f" Created folder: {folder_name}")
    else:
        print(f" Folder already exists: {folder_name}")

def update_job(job_spec):
    jenkins = get_jenkins()
    try:
        job = jenkins[job_spec.name]
        job.update_config(job_spec.config)
        print(f"Updated Job: {job_spec.name}")
    except UnknownJob:
        jenkins.create_job(job_spec.name, job_spec.config)
        print(f"Created Job: {job_spec.name}")
