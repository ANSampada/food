#!/usr/bin/env python3
from update import update_job, ensure_folder, get_jenkins
from jobs import Job

def main():

    jenkins = get_jenkins()

    # Ensure Recipes folder exists
    ensure_folder(jenkins, "Recipes")
    
    # Curry (Freestyle job)
    curry = Job(
        "Recipes/curry",
        "freestyle_template.j2.xml",
        description="Curry build job",
        jira_site="https://jira.example.com",
        conjur_appliance="https://conjur.example.com",
        label_expression="linux-builder",
        repo_url="https://github.com/food-org/curry.git",
        branch="main",
        build_schedule="H/15 * * * *",
        build_steps="make curry",
        notify="dev-team@example.com"
    )
    update_job(curry)

    # Chapati, Samosa, Parata (Pipeline jobs)
    for recipe in ["chapati", "samosa", "parata"]:
        job = Job(
            f"Recipes/{recipe}",
            "pipeline_template.j2.xml",
            description=f"{recipe.capitalize()} pipeline job",
            jira_site="https://jira.example.com",
            conjur_appliance="https://conjur.example.com",
            label_expression="linux-builder",
            repo_url=f"https://github.com/food-org/{recipe}.git",
            branch="main",
            build_steps=f"make {recipe}",
            notify="dev-team@example.com"
        )
        update_job(job)

if __name__ == "__main__":
    main()
