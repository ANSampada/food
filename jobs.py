from jinja2 import Environment, FileSystemLoader

class Job:
    def __init__(self, name, template, **kwargs):
        env = Environment(loader=FileSystemLoader("templates"))
        tmpl = env.get_template(template)
        self.name = name
        self.config = tmpl.render(**kwargs).encode("utf-8")
