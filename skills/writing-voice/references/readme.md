# READMEs

A README says what the thing does and how to use it: not an essay, a build story or a status report. Write the shortest version that does that, then cut again. Median prose is ~230 words; small projects often under 100. Read `exemplars-repo.md` for the feel.

## Leave out

- The author: who built it, why, with what, how it's going. No first-person backstory and no `[Peter: ...]` slot asking for one
- Testing notes, what's been verified, open decisions. Describe intended behavior
- Internals and design rationale, unless the user must act on them
- Exact numbers the reader doesn't need ("shortly before" beat "30 seconds before")

## Write it like this

- Open with one sentence saying what it does: "A simple migration system for CouchDB." "Select values from deeply nested/complex hashes with ease."
- Conventional headings (Usage, Installation, Contributing, License; sub-sections name the feature). Usage usually precedes Installation in libraries
- For a library, show code right away with brief commentary, set up with "Consider..." or "Given...". Use a tool's own form where it fits, like a keybinding table. An app README drops code and describes behavior from the user's side
- Say what happens, including failure: "it will raise a `KeyError` unless a block is provided"
- "you", or tutorial "we" in a walkthrough. Name the project, or "the phone", not "my phone"
- Parentheses for practical notes: "(Don't forget to `require "rspec-hal"` if you are not using bundler.)"
- At most a line of dryness, and only where it's also true about the behavior: Peter kept "Conference rooms and projectors are not people" and cut everything around it. The best jokes live in example code (`will_a_sea_battle_be_fought_tomorrow`)
- Credit others plainly: "Originally written by daddz... Thanks, daddz!"
- Lowercase i on the rare first person; a single "i recommend..." is fine

## Extra checks

1. Cut anything a user wouldn't act on or notice, and anything reading as a status report or author story.
