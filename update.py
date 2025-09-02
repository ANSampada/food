import jenkins

# Folder XML definition
FOLDER_XML = """<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder">
  <description>Recipes folder</description>
</com.cloudbees.hudson.plugins.folder.Folder>"""

JENKINS_URL = "http://10.209.132.115:8080"
USERNAME = "sampada"
PASSWORD = "11e16ad45ee52ec04022655004741c614f"


def get_jenkins():
    """Return a Jenkins server connection"""
    return jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)


def ensure_folder(server, folder_name):
    """Create Jenkins folder if it doesn't exist"""
    if not server.job_exists(folder_name):
        server.create_job(folder_name, FOLDER_XML)
        print(f"Created folder: {folder_name}")
    else:
        print(f"Folder already exists: {folder_name}")


def update_job(job_spec):
    """Create or update a Jenkins job"""
    server = get_jenkins()
    if server.job_exists(job_spec.name):
        server.reconfig_job(job_spec.name, job_spec.config)
        print(f"Updated Job: {job_spec.name}")
    else:
        server.create_job(job_spec.name, job_spec.config)
        print(f"Created Job: {job_spec.name}")
