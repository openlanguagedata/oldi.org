import shutil
from itertools import chain
from pathlib import Path

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape

STATIC_ROOT = Path("./static")
TEMPLATE_ROOT = Path("./templates")
BUILD_ROOT = Path("./build")

# Copy all static content to the build directory
shutil.rmtree(BUILD_ROOT, ignore_errors=True)
shutil.copytree(STATIC_ROOT, BUILD_ROOT)

# The YAML file is used to build the language table at oldi.org/languages.
# We sort it to ensure that the table is sorted, even if the source file isn't.
with open("languages.yaml") as f:
    languages = dict(sorted(yaml.safe_load(f).items()))
shutil.copy("languages.yaml", BUILD_ROOT)

# Compile every template you find
env = Environment(loader=PackageLoader("build"), autoescape=select_autoescape())
for template in TEMPLATE_ROOT.glob("**/*.html"):
    template_path = template.relative_to(TEMPLATE_ROOT)
    tgt_dir = BUILD_ROOT / template_path.parent
    tgt_dir.mkdir(parents=True, exist_ok=True)
    tgt_file = tgt_dir / template.name
    template = env.get_template(str(template_path))
    with open(tgt_file, "wt") as f:
        print(template.render(languages=languages.values()), file=f)
