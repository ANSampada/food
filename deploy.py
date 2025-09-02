from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import UnknownJob

# Connect to Jenkins
def get_jenkins():
    return Jenkins("http://localhost:8080", username="admin", password="admin")

# Deploy job (create or update)
def update_job(name, config_xml):
    jenkins = get_jenkins()
    try:
        job = jenkins[name]
        job.update_config(config_xml)
        print(f"✅ Updated Job: {name}")
    except UnknownJob:
        jenkins.create_job(name, config_xml)
        print(f"🚀 Created Job: {name}")

# Example Freestyle (Curry)
CURRY_XML = """<project>
  <description>Curry build job</description>
  <builders>
    <hudson.tasks.Shell>
      <command>make curry</command>
    </hudson.tasks.Shell>
  </builders>
</project>"""

# Example Pipeline (Chapati)
CHAPATI_XML = """<flow-definition plugin="workflow-job">
  <description>Chapati pipeline job</description>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition">
    <script>
      pipeline {
        agent any
        stages {
          stage('Build') {
            steps {
              sh 'make chapati'
            }
          }
        }
      }
    </script>
    <sandbox>true</sandbox>
  </definition>
</flow-definition>"""

if __name__ == "__main__":
    update_job("curry", CURRY_XML)
    update_job("chapati", CHAPATI_XML)
