import math
import shutil
from datetime import datetime
from distutils.dir_util import copy_tree
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


models_path = Path(__file__).absolute().parent.resolve() / "../models"
template_path = Path(__file__).absolute().parent.resolve() / "web"
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
    "featured": [],
}

default_thumbnail = "https://user-images.githubusercontent.com/5244214/144071726-449a1264-5a63-44b6-91f8-6dba9da02576.png"

for model_file in model_files:
    with model_file.open('r') as f:
        data = yaml.safe_load(f)
    if "meta" not in data:
        continue
    data["name"] = model_file.parent.name
    data["resolution_factor"] = max([math.prod(map(int, input["shape"].split(',')[-2:])) for input in data["meta"]["inputs"]])
    if "thumbnail" not in data["meta"]:
        data["meta"]["thumbnail"] = default_thumbnail
    render_data["categories"][data["task_type"]] = render_data["categories"].get(data["task_type"], 0) + 1
    render_data["models"].append(data)

    if "featured" in data["meta"] and data["meta"]["featured"]:
        render_data["featured"].append(data)


render_data["categories"] = dict(sorted(render_data["categories"].items(), key=lambda item: item[1], reverse=True))
render_data["models"] = sorted(render_data["models"], key=lambda item: (item["meta"].get("featured", False) * 10) + (item["meta"]["thumbnail"] != default_thumbnail), reverse=True)

if output_path.exists():
    shutil.rmtree(output_path)

copy_tree(str(template_path), str(output_path))

with (output_path / "index.html").open("w") as f:
    f.write(index.render(**render_data))
