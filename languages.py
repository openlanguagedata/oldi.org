import argparse
import shutil
from pathlib import Path

import oyaml as yaml
from py_markdown_table.markdown_table import markdown_table

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Utility to perform various tasks with languages.yaml"
    )
    parser.add_argument(
        "--yaml-path", type=Path, default=Path("./resources/languages.yaml")
    )
    subparsers = parser.add_subparsers(dest="command", description="Valid sub-commands")
    parser_sort = subparsers.add_parser("sort", help="Sort the YAML file")
    parser_table = subparsers.add_parser("table", help="Print Markdown tables")
    parser_table.add_argument("dataset", choices="flores+ seed".split())
    args = parser.parse_args()

    # Load the YAML file and sort it
    with open(args.yaml_path) as f:
        languages = dict(sorted(yaml.safe_load(f).items()))

    ######################
    # Sort the YAML file #
    ######################
    if args.command == "sort":
        # Write the sorted YAML to a temp file
        with open(args.yaml_path.with_suffix(".yaml.tmp"), "wt") as f:
            yaml.dump(languages, f, allow_unicode=True)

        # To be absolutely safe, ensure the line counts match
        with open(args.yaml_path) as f:
            n_old = sum(1 for l in f if l.strip())
        with open(args.yaml_path.with_suffix(".yaml.tmp")) as f:
            n_new = sum(1 for l in f if l.strip())
        assert (
            n_old == n_new
        ), "Line mismatch between original and sorted file! Please check manually."

        shutil.move(args.yaml_path.with_suffix(".yaml.tmp"), args.yaml_path)

    #########################
    # Print Markdown tables #
    #########################
    elif args.command == "table":

        def get_issue_list(langdata):
            text = ""
            for i, link in enumerate(langdata.get("issues", []), start=1):
                text += f"[[{i}]]({link}) "
            return text.strip()

        rows = []
        for langdata in languages.values():
            row = {
                "Code": f" `{langdata['iso_639_3']}`",
                "Script": f" `{langdata['iso_15924']}`",
                "Glottocode": f" `{langdata['glottocode']}`",
                "Name": " " + langdata["display_name"],
                "Notes": "",
            }
            if args.dataset == "seed":
                if langdata["datasets"].get("seed") not in ("ok", "warn"):
                    continue
            elif args.dataset == "flores+":
                dev = langdata["datasets"].get("flores_dev")
                devtest = langdata["datasets"].get("flores_devtest")
                if dev not in ("ok", "warn") and devtest not in ("ok", "warn"):
                    continue
                if dev not in ("ok", "warn"):
                    row["Notes"] = " `devtest` only"
                if devtest not in ("ok", "warn"):
                    row["Notes"] = " `dev` only"
            issue_list = get_issue_list(langdata)
            if issue_list:
                if row["Notes"]:
                    row["Notes"] += "; " + issue_list
                else:
                    row["Notes"] = " " + issue_list
            rows.append(row)

        markdown = (
            markdown_table(rows)
            .set_params(
                quote=False,
                row_sep="markdown",
                padding_width=1,
                padding_weight="centerright",
            )
            .get_markdown()
        )
        print(markdown)
