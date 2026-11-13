---
name: confluence-diagrams
description: Publish or edit a PlantUML diagram on a Confluence page in this instance, including the two-step update required to change an existing diagram and mandatory SHA256 verification. Use when asked to put a diagram on a Confluence page, update/fix/restyle a diagram already on a page, or embed any Confluence macro/extension node via the API (extensionType, extensionKey, data-parameters escaping).
---

# PlantUML diagrams in Confluence

Read this whole file before the first `updateConfluencePage` call. Two rules below
cause **silent** failure — the API reports success and the diagram is unchanged.

## Rule 1 — editing an existing diagram takes TWO updates

A single `updateConfluencePage` that replaces an existing extension node **keeps
the previously stored parameters**. The version increments, surrounding prose
changes land, the diagram does not change, and no error is returned. This has
produced two consecutive edits reported as done that were not.

To change a diagram:

1. Update the page body **with the extension node removed entirely**.
2. Re-read the page and confirm the node is gone.
3. Update again, **adding** the extension node with the new parameters.
4. Verify (Rule 2).

Why the single-step replace drops the new parameters is **unexplained**. Observed
asymmetry: replacing a node the *user* had just created in the editor worked
once; replacing a node the *API* created did not. Never rely on the single-step
path, in either case.

## Rule 2 — verify before reporting success

Never report a diagram published or changed without this check:

1. Re-read the page with `contentFormat: "adf"`.
2. Extract `parameters.guestParams.plantumlCode` from the extension node.
3. Compare its SHA256 against the local `.puml` file.
4. Confirm exactly **one** extension node and that `extensionKey` survived.

The ADF response is ~80–100KB and gets persisted to a file instead of returned
inline. Parse that file with python; do not try to read it whole.

```
python3 scripts/verify_page_diagram.py <adf-response.json> <diagram.puml>
```

It prints both hashes and PASS/FAIL, and diffs live vs local on mismatch.

## The macro

This instance's PlantUML macro is a Forge (Atlassian Ecosystem) extension:

- `extensionType`: `com.atlassian.ecosystem`
- `extensionKey`:
  `ef9c2b02-5cf5-49e3-8daa-1f9030cd772d/852e0f37-86e2-489f-8ecb-f8eac32a9bff/static/plantuml-diagram`
- `parameters`: `{"layout":"extension","guestParams":{"plantumlCode":"<puml source>"}}`

In HTML+ (`contentFormat: "html"` on `updateConfluencePage`) it is one div:

```html
<div data-type="extension"
     data-extension-type="com.atlassian.ecosystem"
     data-extension-key="ef9c2b02-5cf5-49e3-8daa-1f9030cd772d/852e0f37-86e2-489f-8ecb-f8eac32a9bff/static/plantuml-diagram"
     data-parameters="<escaped JSON>"></div>
```

`scripts/puml_to_params.py <file.puml> --div` emits exactly that line.

### Rediscovering the key

The key is instance-specific and could change. If the diagram stops rendering or
you are working in a different instance:

1. Ask the user to insert the macro manually once, via `/plantuml` in the editor,
   and save.
2. Read that page with `contentFormat: "adf"`.
3. Pull `extensionType`, `extensionKey`, and `parameters` off the extension node.

Do **not** try CQL for discovery. `macro = "plantuml"` returns nothing for Forge
macros even when the macro is in use on the page — it is useless here.

## Escaping — always scripted

Chain: PlantUML source → JSON string → HTML attribute escape. Generate it:

```
python3 scripts/puml_to_params.py diagram.puml          # data-parameters value
python3 scripts/puml_to_params.py diagram.puml --div    # full <div>
python3 scripts/puml_to_params.py diagram.puml --json   # raw JSON, for ADF form
```

The script asserts a byte-for-byte round trip and refuses sources containing
named HTML entities. Two traps it guards:

- **No named HTML entities in diagram text.** Confluence's HTML parser decodes
  only `&amp; &lt; &gt; &quot;`. Named entities (`&mdash;` `&middot;` `&rarr;`
  `&rArr;`) pass through as **literal text** and render inside the diagram. Put
  real Unicode characters in the `.puml`: — · → ⇒.
- **PlantUML's `\n` label escape is a literal backslash-n**, not a newline —
  e.g. `participant "Pusher\n(one per type)"`. It must survive as `\\n` through
  JSON encoding. `json.dumps` gets this right; hand-escaping does not. This is
  the single best reason never to build the attribute by hand.

## Publishing a NEW diagram

1. Write the `.puml` in the repo — that file is the source of truth.
   Apply the user's theme with the **`plantuml-theme` skill**
   (`/Users/pwilliams/.claude/skills/plantuml-theme/`): header pragmas +
   `autonumber` at the top, cosmetic `skinparam`/`<style>` at the bottom. Load
   that skill; do not reproduce its contents from memory.
2. Render locally and look at it (see Local rendering) before publishing.
3. `python3 scripts/puml_to_params.py diagram.puml --div`
4. `updateConfluencePage` with `contentFormat: "html"`, page body = the prose
   plus that div.
5. Verify (Rule 2).

## Editing an EXISTING diagram

1. **Pull live source first.** The user edits diagrams directly in Confluence.
   Read the page with `contentFormat: "adf"`, extract
   `parameters.guestParams.plantumlCode`, diff it against the local `.puml`, and
   sync local from live. Skipping this silently reverts the user's edits.
2. Make the change in the local `.puml`.
3. Render locally and check it.
4. Two-step update per Rule 1: update without the div, confirm it is gone, then
   update with the new div from `puml_to_params.py --div`.
5. Verify (Rule 2).

## Local rendering

- `plantuml` is at `/opt/homebrew/bin/plantuml`.
- **`-tpng` fails in this sandbox**: Java ImageIO cannot create its temp cache
  file (`Operation not permitted` under `/var/folders/...`). Use `-tsvg`.

```
/opt/homebrew/bin/plantuml -tsvg diagram.puml
rsvg-convert --background-color=white -w 1400 diagram.svg -o diagram.png
```

`--background-color=white` is required: PlantUML declares its white background
in a root `style` attribute that rsvg ignores, so output is otherwise on black.
Then Read the PNG to actually look at the diagram.

### Layout constraint

**Long message labels overflow the computed canvas and get clipped** at the
edges. `skinparam wrapWidth 1000` does not prevent it. Keep message labels
short and put the detail in `note over X` / `note over A, B` blocks — PlantUML
sizes notes correctly.

## Never use handwritten

`handwritten` (`skinparam handwritten true`, `!option handwritten true`) is
banned in every diagram, including wireframes. See the `plantuml-theme` skill.
Grep the `.puml` for it before publishing.

## Defaults

The user's theme is sequence-diagram oriented (`!pragma teoz true`,
`sequenceMessageSpan`, `autonumber`), so **sequence diagrams are the default
form** unless the user asks otherwise.
