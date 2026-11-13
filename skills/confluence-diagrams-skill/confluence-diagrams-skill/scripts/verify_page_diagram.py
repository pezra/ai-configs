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


def deep_expand(node, depth=0):
    """Recursively parse embedded JSON strings so nested envelopes get traversed.

    The MCP getConfluencePage response is a [{"type":"text","text":...}] array
    whose `text` holds the whole page object as a JSON *string*; inside that,
    `body` is a plain ADF dict. Other shapes nest the ADF under
    body.atlas_doc_format.value as a JSON string. Expanding any embedded JSON at
    any key covers both without having to know which one applies.
    """
    if depth > 8:
        return node
    if isinstance(node, dict):
        return {k: deep_expand(v, depth + 1) for k, v in node.items()}
    if isinstance(node, list):
        return [deep_expand(v, depth + 1) for v in node]
    if isinstance(node, str):
        s = node.lstrip()
        if s[:1] in ("{", "["):
            try:
                return deep_expand(json.loads(node), depth + 1)
            except json.JSONDecodeError:
                return node
    return node


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
    doc = deep_expand(json.loads(raw))
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
