import yaml
from jinja2 import Environment, FileSystemLoader

def load_data_from_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def render_template(template_path, data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    return template.render(data)

def main():
    data = load_data_from_yaml('data.yml')
    vhosts_conf = render_template('vhosts.j2', data)
    with open('vhosts.conf', 'w') as file:
        file.write(vhosts_conf)

if __name__ == "__main__":
    main()
