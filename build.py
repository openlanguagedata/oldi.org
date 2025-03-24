import shutil
from itertools import chain
from pathlib import Path

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
import mistune

STATIC_ROOT = Path("./static")
TEMPLATE_ROOT = Path("./templates")
BUILD_ROOT = Path("./build")
CARDS_ROOT = Path("dataset_cards")
# TODO: maybe git submodule from the other repositories, instead of copying the cards directory
SEED_CARDS_URL = "https://huggingface.co/datasets/openlanguagedata/oldi_seed/blob/main/dataset_cards"
FLORES_CARDS_URL = "https://huggingface.co/datasets/openlanguagedata/flores_plus/blob/main/dataset_cards"

# Copy all static content to the build directory
shutil.rmtree(BUILD_ROOT, ignore_errors=True)
shutil.copytree(STATIC_ROOT, BUILD_ROOT)

# The YAML file is used to build the language table at oldi.org/languages.
# We sort it to ensure that the table is sorted, even if the source file isn't.
with open("languages.yaml") as f:
    languages = dict(sorted(yaml.safe_load(f).items()))
shutil.copy("languages.yaml", BUILD_ROOT)

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
            print(f"Warning: language `{lang}` was found in {data_name} dataset cards, but not in languages.yaml; skipping it.")
    data2langs2cards[data_name] = lang2cards

md_renderer = mistune.create_markdown(
    escape=False,
    plugins=['strikethrough', 'footnotes', 'table', 'url']
)

# Compile every template you find
env = Environment(loader=PackageLoader("build"), autoescape=select_autoescape())
for template in TEMPLATE_ROOT.glob("**/*.html"):
    template_path = template.relative_to(TEMPLATE_ROOT)
    tgt_dir = BUILD_ROOT / template_path.parent
    tgt_dir.mkdir(parents=True, exist_ok=True)
    template = env.get_template(str(template_path))

    if template_path.name == "dataset_card.html":
        # the dataset card template is applied for every dataset card
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
                    print(template.render(card_content=card_html, lang=lang, orig_url=orig_url), file=f)
    else:
        # for all other templates, render them just once
        tgt_file = tgt_dir / template.name
        with open(tgt_file, "wt") as f:
            print(template.render(languages=languages.values()), file=f)
