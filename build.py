from pathlib import Path
import shutil
from itertools import chain

from jinja2 import Environment, PackageLoader, select_autoescape

STATIC_ROOT = Path("./static")
TEMPLATE_ROOT = Path("./templates")
BUILD_ROOT = Path("./build")

shutil.rmtree(BUILD_ROOT, ignore_errors=True)
shutil.copytree(STATIC_ROOT, BUILD_ROOT)


env = Environment(loader=PackageLoader("build"), autoescape=select_autoescape())

for template in TEMPLATE_ROOT.glob("**/*.html"):
    template_path = template.relative_to(TEMPLATE_ROOT)
    tgt_dir = BUILD_ROOT / template_path.parent
    tgt_dir.mkdir(parents=True, exist_ok=True)
    tgt_file = tgt_dir / template.name
    template = env.get_template(str(template_path))
    with open(tgt_file, "wt") as f:
        print(template.render(), file=f)