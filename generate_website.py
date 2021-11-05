import math
import shutil
from datetime import datetime
from distutils.dir_util import copy_tree
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


models_path = Path(__file__).absolute().parent.resolve() / "models"
template_path = Path(__file__).absolute().parent.resolve() / "template"
output_path = Path(__file__).absolute().parent.resolve() / "public"
env = Environment(
    loader=FileSystemLoader(template_path),
    autoescape=select_autoescape()
)
index = env.get_template("index.html")

model_files = models_path.rglob("model.yml")

render_data = {
    "categories": {},
    "models": [],
}

for model_file in model_files:
    with model_file.open('r') as f:
        data = yaml.safe_load(f)
    if "meta" not in data:
        continue
    data["name"] = model_file.parent.name
    data["resolution_factor"] = max([math.prod(map(int, input["shape"].split(',')[-2:])) for input in data["meta"]["inputs"]])
    render_data["categories"][data["task_type"]] = render_data["categories"].get(data["task_type"], 0) + 1
    render_data["models"].append(data)

render_data["categories"] = dict(sorted(render_data["categories"].items(), key=lambda item: item[1], reverse=True))

if output_path.exists():
    shutil.rmtree(output_path)

copy_tree(str(template_path), str(output_path))

with (output_path / "index.html").open("w") as f:
    f.write(index.render(**render_data))
