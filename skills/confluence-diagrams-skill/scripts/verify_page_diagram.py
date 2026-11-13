#!/usr/bin/env python3
"""Verify a published Confluence diagram matches a local .puml file.

Input is the ADF response file that `getConfluencePage` (contentFormat: "adf")
persisted to disk — that response is ~80-100KB and is written to a file rather
than returned inline, so parse the file, never try to read it whole.

Usage:
    python3 verify_page_diagram.py <adf-response.json> <diagram.puml>

Exits non-zero and prints what differs if verification fails.
"""

import hashlib
import json
import sys

EXPECTED_TYPE = "com.atlassian.ecosystem"
EXPECTED_KEY_SUFFIX = "static/plantuml-diagram"


def walk(node):
    """Yield every dict node in an arbitrarily nested ADF structure."""
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


def find_extensions(root):
    out = []
    for n in walk(root):
        if not isinstance(n, dict):
            continue
        if n.get("type") in ("extension", "bodiedExtension", "inlineExtension"):
            out.append(n)
        elif "extensionKey" in n.get("attrs", {}):
            out.append(n)
    # de-duplicate by identity
    seen, uniq = set(), []
    for n in out:
        if id(n) not in seen:
            seen.add(id(n))
            uniq.append(n)
    return uniq


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    adf_path, puml_path = sys.argv[1], sys.argv[2]

    with open(adf_path, encoding="utf-8") as fh:
        raw = fh.read()
    doc = json.loads(raw)
    # The ADF body may be a JSON string nested inside the API envelope.
    for n in list(walk(doc)):
        if isinstance(n, dict):
            for k in ("value", "representation_value", "atlas_doc_format"):
                v = n.get(k)
                if isinstance(v, str) and v.lstrip().startswith("{"):
                    try:
                        n[k] = json.loads(v)
                    except json.JSONDecodeError:
                        pass

    exts = find_extensions(doc)
    problems = []

    if len(exts) != 1:
        problems.append(f"expected exactly 1 extension node, found {len(exts)}")

    if not exts:
        print("FAIL\n  " + "\n  ".join(problems))
        sys.exit(1)

    attrs = exts[0].get("attrs", exts[0])
    ext_type = attrs.get("extensionType")
    ext_key = attrs.get("extensionKey", "")
    if ext_type != EXPECTED_TYPE:
        problems.append(f"extensionType is {ext_type!r}, expected {EXPECTED_TYPE!r}")
    if not ext_key.endswith(EXPECTED_KEY_SUFFIX):
        problems.append(f"extensionKey does not end with {EXPECTED_KEY_SUFFIX!r}: {ext_key!r}")

    params = attrs.get("parameters") or {}
    if isinstance(params, str):
        params = json.loads(params)
    live = (params.get("guestParams") or {}).get("plantumlCode")
    if live is None:
        problems.append("no parameters.guestParams.plantumlCode on the extension node")
        print("FAIL\n  " + "\n  ".join(problems))
        sys.exit(1)

    with open(puml_path, encoding="utf-8") as fh:
        local = fh.read()

    live_sha = hashlib.sha256(live.encode("utf-8")).hexdigest()
    local_sha = hashlib.sha256(local.encode("utf-8")).hexdigest()

    print(f"live  sha256 {live_sha}  ({len(live)} chars)")
    print(f"local sha256 {local_sha}  ({len(local)} chars)")

    if live_sha != local_sha:
        problems.append("plantumlCode does not match the local .puml file")
        import difflib

        diff = list(
            difflib.unified_diff(
                local.splitlines(), live.splitlines(), "local", "live", lineterm="", n=1
            )
        )
        print("\n".join(diff[:60]))

    if problems:
        print("FAIL\n  " + "\n  ".join(problems))
        sys.exit(1)
    print("PASS: one extension node, key intact, plantumlCode matches local source")


if __name__ == "__main__":
    main()
