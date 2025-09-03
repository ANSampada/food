import os
from jinja2 import Environment, FileSystemLoader

class Job:
    def __init__(self, name, template, **kwargs):
        # Find the directory of this file (jobs.py)
        template_dir = os.path.join(os.path.dirname(__file__), "templetes")
        env = Environment(loader=FileSystemLoader(template_dir))
        
        tmpl = env.get_template(template)
        self.name = name
        self.config = tmpl.render(**kwargs)
