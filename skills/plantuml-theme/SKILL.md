---
name: plantuml-theme
description: Apply the user's default PlantUML theme/preamble (teoz, autonumber, fonts, sequence styling). The cosmetic boilerplate sits at the BOTTOM of the diagram. Use whenever creating a new PlantUML/.puml diagram, or when the user asks to apply, restore, or normalize their default PlantUML theme/styling on an existing diagram.
---

# PlantUML Default Theme

The user's standard boilerplate is split across two files in this skill's
directory:

- `theme-header.puml` — the **top** block: `@startuml`, the `!pragma`
  directives, `autonumber`, and the two font `skinparam`s. These are
  position-sensitive and MUST stay at the top (`autonumber` only numbers
  messages that appear after it; see the font note below).
- `theme-footer.puml` — the **bottom** block: the remaining cosmetic `skinparam`
  settings, the `<style>` block, and the closing `@enduml`. The user wants this
  styling boilerplate tucked at the bottom of the diagram, out of the way.

So a finished diagram looks like:

```
<contents of theme-header.puml>

  ... diagram body (participants, messages, notes, dividers) ...

<contents of theme-footer.puml>
```

## Never use handwritten

`skinparam handwritten true` and `!option handwritten true` are **banned** in
every diagram, every diagram type, with no exceptions. The user finds the
output terrible. This holds for wireframes and "sketch quality" requests too:
get the sketch feel from layout, simple shapes, and the theme fonts, never from
the handwritten option.

- Do not add it to a new diagram, even when asked for a sketch or wireframe.
- When editing an existing diagram, remove it if present and say so.
- Before publishing or rendering, run `grep -n handwritten <file>.puml`. Any hit
  is a failure to fix first.

## When creating a NEW diagram

1. Read `theme-header.puml` and `theme-footer.puml`.
2. Write the header contents verbatim (do not reword pragmas, the autonumber
   format string, font lists, or the style block).
3. Add the diagram body.
4. Append the footer contents verbatim (it ends with `@enduml`).

## When applying the theme to an EXISTING diagram

1. Read both theme files.
2. Identify the diagram's current boilerplate — the `@startuml`, `!pragma`,
   `autonumber`, `skinparam`, `<style>…</style>`, and `@enduml` directives —
   wherever they currently sit.
3. Remove that boilerplate and re-layout the file as: header block → diagram
   body → footer block, using the contents of the two theme files.
4. Preserve the diagram body (participants, messages, notes, `...` dividers,
   `|||` spacers) unchanged.
5. Where the diagram set a directive the theme also sets (e.g. a different
   `wrapWidth`), the theme value wins — that's the point of normalizing.

## Notes

- The split exists because `autonumber`, the `!pragma` engine directives, and
  the font `skinparam`s are position-sensitive; the rest of the cosmetics live
  in the footer.
- **Sequence diagrams ignore `skinparam defaultFontName` / `defaultFontSize`
  placed after the diagram body.** Participants, messages and notes silently
  render in `sans-serif` while the title alone gets the theme font. That is why
  those two lines sit in the header. Class and entity diagrams honour them from
  either position, so this is easy to miss when checking one diagram type.
  Verify with `grep -o 'font-family="[^"]*"' out.svg | sort | uniq -c` — every
  text element should report the theme font list, not `sans-serif`.
- `skinparam wrapWidth 1000` in the footer is subject to the same rule and has
  no effect on sequence diagrams. It stays in the footer deliberately: hoisting
  it re-wraps every hand-formatted note and changes existing layouts. Diagrams
  here wrap their own long note text with explicit line breaks instead.
- A non-sequence diagram (class, entity, ERD) cannot use the header block — the
  sequence pragmas and `autonumber` put PlantUML into sequence mode and
  `entity Foo { }` then fails to parse. Give those diagrams the font
  `skinparam`s and the footer cosmetics only.
- To change the defaults going forward, edit `theme-header.puml` /
  `theme-footer.puml` — do not hardcode the blocks anywhere else.
