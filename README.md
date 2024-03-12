# oldi.org

This is the website <https://oldi.org>. We use the Jinja2 templates in `templates/` to avoid code duplication of common elements such as HTML page headers. Static files are located in `static/`.

## Building

The `build.py` script builds the website into the build directory `build/`. This is the directory that is served by our host (currently Cloudflare Pages). When a new commit is pushed to GitHub, the host will automatically run the build script and update the public-facing site based on what is in the build directory.

The build process is straightforward:
1. We load all language metadata from `languages.yaml`, and copy it to the build directory (so it can be accessed by the public).
2. We copy all static content in `static/` to the build directory.
3. We compile all templates in `templates/` to the build directory.

### Local builds

For local builds, first install the required packages, including the development dependencies:
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

To build content and spin up a local HTTP server:
```
python build.py && python -m http.server --directory build
```

This command should be re-run when the source is changed. TODO: auto-reload.

## Utilities

The script `languages.py` can perform tasks on the YAML script.

`python languages.py sort` will automatically sort and overwrite the YAML file.

`python languages.py table {flores+,seed}` will print a Markdown table for a given dataset which can then be included in the README of its GitHub repo.
