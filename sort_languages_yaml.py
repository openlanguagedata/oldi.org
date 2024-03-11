import shutil

import oyaml as yaml

# Load the YAML file
with open("languages.yaml") as f:
    languages = yaml.safe_load(f)

# Sort it by key and write to a temp file
languages = dict(sorted(languages.items()))
with open("languages.yaml.tmp", "wt") as f:
    yaml.dump(languages, f, allow_unicode=True)

# To be absolutely safe, ensure the line counts match
with open("languages.yaml") as f:
    n_old = sum(1 for l in f if l.strip())
with open("languages.yaml.tmp") as f:
    n_new = sum(1 for l in f if l.strip())
assert (
    n_old == n_new
), "Line mismatch between original and sorted file! Please check manually."

shutil.copy("languages.yaml.tmp", "languages.yaml")
