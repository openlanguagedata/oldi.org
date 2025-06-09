import shutil
from pathlib import Path
import re

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
import mistune
from mistune.directives import FencedDirective, Admonition
from weasyprint import HTML, CSS

STATIC_ROOT = Path("./static")
TEMPLATE_ROOT = Path("./templates")
BUILD_ROOT = Path("./build")
CARDS_ROOT = Path("./dataset_cards")
RESOURCES_ROOT = Path("./resources")

REPO_URL = "https://github.com/openlanguagedata/oldi.org/tree/main"
# TODO: maybe git submodule from the other repositories, instead of copying the cards directory
SEED_CARDS_URL = (
    "https://huggingface.co/datasets/openlanguagedata/oldi_seed/blob/main/dataset_cards"
)
FLORES_CARDS_URL = "https://huggingface.co/datasets/openlanguagedata/flores_plus/blob/main/dataset_cards"

# Copy all static content to the build directory
shutil.rmtree(BUILD_ROOT, ignore_errors=True)
shutil.copytree(STATIC_ROOT, BUILD_ROOT)

# The YAML file is used to build the language table at oldi.org/languages.
# We sort it to ensure that the table is sorted, even if the source file isn't.
with open(RESOURCES_ROOT / "languages.yaml") as f:
    languages = dict(sorted(yaml.safe_load(f).items()))

# Read the FLORES+ and Seed dataset cards and attach them to the languages
data2langs2cards = {}  # {dataset name => lang name => dataset card}
for data_cards_path in CARDS_ROOT.iterdir():
    data_name = data_cards_path.name  # flores or seed
    lang2cards = {}
    for lang_path in data_cards_path.iterdir():
        lang = lang_path.stem
        with open(lang_path, "r") as f:
            card_md = f.read()
        if lang in languages:
            lang2cards[lang] = card_md
            languages[lang][f"{data_name}_card"] = f"/cards/{data_name}/{lang}.html"
        else:
            print(
                f"Warning: language `{lang}` was found in {data_name} dataset cards, but not in languages.yaml; skipping it."
            )
    data2langs2cards[data_name] = lang2cards

md_renderer = mistune.create_markdown(
    escape=False,
    plugins=[
        "strikethrough",
        "footnotes",
        "table",
        "url",
        FencedDirective([Admonition()]),
    ],
)

# A function to convert GFM-style admonitions since our renderer doesn't support them.
# We stick to the GFM syntax since we're hosting our markdown files on GitHub.
def convert_gfm_admonitions(md):
    def replace_admonitions(match):
        title = match.group(1).title() + "!"
        lines = match.group(2).strip().split("\n")
        content = " ".join(line[2:] for line in lines if line.startswith("> "))
        return f'<div class="box"><strong>{title}</strong> {content}</div>\n'

    pattern = r"> !\[(CAUTION|NOTE)\]\n((?:> .*\n)*)"
    return re.sub(pattern, replace_admonitions, md, flags=re.M)


# Compile the guidelines from the markdown source
with open(RESOURCES_ROOT / "translation-guidelines.md") as f:
    guidelines_html = md_renderer(convert_gfm_admonitions(f.read()))
    css = CSS(filename=STATIC_ROOT / "style.css")
    HTML(string=guidelines_html).write_pdf(
        BUILD_ROOT / "translation-guidelines.pdf", stylesheets=[css]
    )

# Compile the main templates
env = Environment(loader=PackageLoader("build"), autoescape=select_autoescape())
for template_name in "guidelines index languages related values".split():
    template_path = Path(f"./{template_name}.html")
    tgt_dir = BUILD_ROOT / template_path.parent
    tgt_dir.mkdir(parents=True, exist_ok=True)
    template = env.get_template(str(template_path))
    tgt_file = tgt_dir / template.name
    with open(tgt_file, "wt") as f:
        print(
            template.render(
                languages=languages.values(),
                repo_url=REPO_URL,
            ),
            file=f,
        )

# Compile the dataset cards
template = env.get_template("dataset_card.html")
for data_name, lang2cards in data2langs2cards.items():
    cards_tgt_dir = tgt_dir / "cards" / data_name
    cards_tgt_dir.mkdir(parents=True, exist_ok=True)
    for lang_id, card_md in lang2cards.items():
        card_html = md_renderer(card_md)
        tgt_file = cards_tgt_dir / f"{lang_id}.html"
        lang = languages[lang_id]
        if data_name == "seed":
            orig_url = f"{SEED_CARDS_URL}/{lang_id}.md"
        elif data_name == "flores":
            orig_url = f"{FLORES_CARDS_URL}/{lang_id}.md"
        else:
            orig_url = None
        with open(tgt_file, "wt") as f:
            print(
                template.render(card_content=card_html, lang=lang, orig_url=orig_url),
                file=f,
            )
