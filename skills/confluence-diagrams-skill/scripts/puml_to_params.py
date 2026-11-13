#!/usr/bin/env python3
"""Turn a .puml file into the escaped data-parameters value for the Confluence
Forge PlantUML macro.

Usage:
    python3 puml_to_params.py path/to/diagram.puml            # print attr value
    python3 puml_to_params.py path/to/diagram.puml --div      # print whole <div>
    python3 puml_to_params.py path/to/diagram.puml --json     # print raw JSON (ADF form)
    python3 puml_to_params.py path/to/diagram.puml --sha       # print sha256 of source

Never hand-escape. The chain is PlantUML source -> JSON string -> HTML attribute
escape, and PlantUML's own `\\n` label escape is a literal backslash-n that must
survive as \\\\n through JSON encoding.
"""

import argparse
import hashlib
import html
import json
import re
import sys

EXTENSION_TYPE = "com.atlassian.ecosystem"
EXTENSION_KEY = (
    "ef9c2b02-5cf5-49e3-8daa-1f9030cd772d/"
    "852e0f37-86e2-489f-8ecb-f8eac32a9bff/"
    "static/plantuml-diagram"
)

NAMED_ENTITY = re.compile(r"&[a-zA-Z]+;")


def build(code: str):
    """Return (json_string, html_attr_value), asserting a clean round trip."""
    bad = sorted(set(NAMED_ENTITY.findall(code)))
    if bad:
        sys.exit(
            "ERROR: named HTML entities found in source: "
            + ", ".join(bad)
            + "\nConfluence decodes only &amp; &lt; &gt; &quot;. Named entities "
            "pass through as literal text and render inside the diagram.\n"
            "Replace them with real Unicode characters (e.g. — · → ⇒)."
        )

    params = {"layout": "extension", "guestParams": {"plantumlCode": code}}
    j = json.dumps(params, ensure_ascii=False, separators=(",", ":"))
    attr = html.escape(j, quote=True)

    # Round trip: unescape the attribute, parse the JSON, recover the source byte for byte.
    recovered = json.loads(html.unescape(attr))["guestParams"]["plantumlCode"]
    assert recovered == code, "round trip failed: escaped value does not decode to source"
    return j, attr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("puml")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--div", action="store_true", help="emit the full extension <div>")
    group.add_argument("--json", action="store_true", help="emit the raw JSON parameters object")
    group.add_argument("--sha", action="store_true", help="emit sha256 of the source only")
    args = ap.parse_args()

    with open(args.puml, encoding="utf-8") as fh:
        code = fh.read()

    if args.sha:
        print(hashlib.sha256(code.encode("utf-8")).hexdigest())
        return

    j, attr = build(code)

    if args.json:
        print(j)
    elif args.div:
        print(
            '<div data-type="extension"'
            f' data-extension-type="{EXTENSION_TYPE}"'
            f' data-extension-key="{EXTENSION_KEY}"'
            f' data-parameters="{attr}"></div>'
        )
    else:
        print(attr)

    print(
        f"# ok: round trip verified, {len(code)} source chars, "
        f"sha256={hashlib.sha256(code.encode('utf-8')).hexdigest()}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
