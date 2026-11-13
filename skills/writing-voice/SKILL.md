---
name: writing-voice
description: Write or rewrite text in Peter Williams's (pezra's) voice. Use this whenever Peter asks for something that will go out under Peter's name, such as a blog post, essay, technical argument, design doc, ADR, RFC, API reference, incident report, team standard, Jira ticket, bug report, Confluence page, resume, cover letter, README, repo description, PR description, commit message, team message, Slack or email draft, or social post, or says "in my voice", "sound like me", "write this like i would", or "make this less AI". Also use it for editing, tightening, de-hedging or de-AI-ing Peter's drafts, even if voice isn't mentioned. Don't use it for Claude's own replies or for code.
---

# Peter's writing voice

Derived from barelyenough.org (2005–2022, settled from 2009 on), about 40 of Peter's Confluence pages (2023–2026), Peter's resume, Peter's public READMEs and commit history, and Peter's own edits of drafts made with this skill.

In one line: an experienced engineer thinking out loud, plainly, who says what they actually think, shows why, and admits where it might not hold.

## Read the guide for what you're writing

This file has the rules every piece shares. The rest lives in reference files, and the voice doesn't come through without them, so read the ones listed before drafting.

| Writing | Read first |
|---|---|
| Commit message, PR description, repo description | Nothing more; see below |
| README | `references/readme.md` and `references/exemplars-repo.md` |
| Blog post, essay, technical argument | `references/prose.md` and `references/exemplars-prose.md` |
| Team message, email, Slack, short or social post, de-AI edit of Peter's draft | `references/prose.md` (the exemplars' "Short posts" section helps for very short pieces) |
| Design doc, ADR, RFC, API reference, incident report, team standard, ticket, bug report, Confluence page, working notes | `references/work-docs.md` |
| Resume, cover letter | `references/resume.md` |

A README written in the blog voice came back as "too wordy and personal", so don't borrow from `prose.md` for repo writing. Work documents are impersonal in the same way, so don't borrow the blog's first-person opinion or characteristic moves for them either. A design note meant to persuade peers, rather than specify a system, is a technical argument.

## Don't invent anything

- **Don't invent Peter's life.** Use only experiences, opinions, people and results Peter gave you or that are in the source material. Don't elaborate on the ones you were given either: "we had a lot of flaky tests" doesn't license how they got that way or what fixing them took. Where a passage needs more, write `[Peter: did you see this in practice?]`. Under Peter's name, an invented detail is a false claim.
- **Don't assign opinions.** If Peter's view matters and wasn't given, ask, or flag the draft as a guess.
- **Facts and arguments are handled differently.** A new fact about what happened, what Peter did, or what Peter saw never goes in the draft, even with a note; put a `[Peter: ...]` slot there instead. A supporting argument Peter didn't give may go in, but list it on handover so Peter can check it. A wry remark that follows from what you were told needs neither.

## First person

Lowercase **i** mid-sentence, including i'm, i'll, i've: "Personally, i find all of the existing options wanting." Capital **I** to start any sentence, line or paragraph, including right after a salutation. It's the most recognizable marker and applies everywhere except formal external documents such as resumes and cover letters.

## AI habits that break this voice

Most have zero or near-zero occurrences in Peter's writing:

- "moreover", "furthermore", "delve", "leverage" (verb), "robust", "landscape", "navigate", "crucial", "game-changer", "at its core"
- Hedging adverbs: "arguably", "somewhat", "potentially", "in some sense"
- "It's not X, it's Y" / "This isn't about X. It's about Y."
- Reflexive triads and stacked parallel sentences
- Punchy one-line paragraphs and staccato fragments for drama
- Em dashes as a connector (dashes are rare in Peter's writing, and they're spaced en dashes ( – ) when they appear)
- Bullets standing in for an argument, bolded lead-ins on every point, emoji, callout boxes, "TL;DR", headings phrased as clever promises
- Opening on a broad truth about "today's world" or with "this document describes"; closing with a summary or a call to reflection
- Over-even balance. Peter picks a side

## Commit messages

Short subject, no period, lowercase imperative, code in backticks: "support relative links", "fix `mix release`". The subject names the feature or the bug fixed, not the code change ("fix csv export dropping rows with newlines", not "parse csv export with `NimbleCSV`"). An occasional joke is fine: "reformat everything ¯\_(ツ)_/¯".

Then a body of two or three sentences saying why: the feature added, or the bug's symptom as a user would see it, and the cause in a clause. Don't narrate the diff or mention the tests. Peter wants this body even though older commits lack it; trivial changes ("bump version") can skip it. Follow a repo's existing style if different, and keep any session-required attribution lines.

## PR descriptions

Same as a commit body, a little longer: why, in one to three sentences, then any caveat the reviewer needs on its own line. No summary of the diff and no list of files touched. Use the repo's PR template if it has one.

## Repo descriptions

Under ten words, imperative or fragment, no final period: "Use HAL APIs easily", "Three value logic for Elixir", "simple file based queue in Ruby". The one place a joke can carry the line: "scaffolding for chronic meeting missers".

## Check before delivering

1. Fix capital "I" (I'm, I'll, I've) mid-sentence. Then capitalize every "i" that starts a sentence, line or paragraph.
2. Search for the AI-habit words and patterns, and for em dashes.
3. Trace every first-person experience, detail and opinion to what Peter provided; flag the rest as `[Peter: ...]` and mention the flags on handover.
4. Run the extra checks at the end of the guide you read.
