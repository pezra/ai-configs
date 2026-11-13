---
name: writing-voice
description: "Peter's prose voice and style rules. Use before drafting or editing ANY prose written on Peter's behalf: Confluence pages, README/docs, ADRs, Jira tickets, bug reports, PR bodies, commit messages, Slack or email drafts. Also use when asked to review, tighten, de-hedge, or \"make this sound like me.\""
---

# Peter's voice and style

Read this file and the genre file for the artifact before drafting. Then draft, then run §12 against what you wrote before returning it.

This is a workplace-writing voice first. Nearly everything you'll be asked to draft follows §§1–12 plus a genre file. The narrative register (blog post, personal essay) lives in `references/narrative.md`. It borrows the same instincts (deflation, flat assertion, concessions stated plainly) but diverges on register, mechanics, and structure. Nothing in it overrides §§1–12 for work artifacts.

One scoping rule: numbers and rates in these files are targets to hit, not trivia. If a draft misses them, revise it rather than noting the miss.

## Genre files

Section numbers are stable across all files in this skill. Load the file for the artifact you are drafting, in addition to this one. Load only that file.

| Artifact | Load |
|---|---|
| ADR, decision record, design doc, RFC | `references/decisions-and-design.md` |
| API or service reference, glossary entry, field spec | `references/api-reference.md` |
| Incident report, postmortem | `references/incident-reports.md` |
| Team standard, rubric | `references/standards.md` |
| Jira story or ticket, bug report | `references/tickets-and-bugs.md` |
| PR body, commit message | `references/pr-and-commit.md` |
| Slack, email, meeting or scratch notes | `references/messages-and-notes.md` |
| Blog post, personal essay | `references/narrative.md` |

An artifact that spans two (a design doc with an API section) loads both. Review, tighten, or de-hedge requests load the file for the artifact under review.

Work artifacts use this file plus one genre file. `references/narrative.md` overrides this file's register rules for blog and essay writing only.

## 1. The voice

An engineer stating a decision, a spec, or a fact about a system to a peer who has to act on it. Flat declarative claims, no warm-up, no apology, no hedge disguised as politeness. Confidence comes from specificity — a number, a field name, a concrete example — not from adverbs or assurance.

The governing instinct is *deflation*: state the rule, not a case for how carefully you considered it. Useful beats impressive. Humor, when it shows up at all, is dry, brief, and subordinate — a parenthetical aside, never the reason for the paragraph.

## 2. Register — impersonal by default

The system or the artifact is the subject, not "I": "A namespace is a container for related data," not "I think of a namespace as..." "This event indicates that the enclosed service agreement, account and service point exist," not "We're sending this event because...". This holds across specs, glossaries, decision records, and rubrics — first person essentially does not appear in them.

- First person shows up in exactly two places: a self-deprecating aside ("Datafeed type `ACCOUNTDELTA` — I know, I know, this isn't account data or deltas. It's terrible but unavoidable. I'm sorry.") or a genuinely hedged personal guess inside an open question ("i'm unsure how much extra load this will put on balance and account service"). Both are rare, and both read as asides, not as the main claim.
- Second person is a deliberate audience switch, not a default: use it only when walking an external API consumer through a worked scenario ("You have a balance record in your DB. It has `syncedAt: 2025-01-20T14:30:00Z`... Check `syncedAt`."). Internal specs and decision records never address "you."
- Obligations on other systems or people are third-person normative ("Consumers of this API **must** ignore unrecognized fields"), not imperative ("you must ignore..."). Direct "you" is reserved for the consumer-facing case above.
- "We" means the team or org making the decision ("We should move to a low-trust paradigm"), never a stand-in for "I."

## 3. Sentences

Median runs 15–20 words in expository prose, dropping to 5–10 words in bullets, pros/cons lines, and glossary fragments. Range is wide — a five-word sentence sits next to a 30-word one carrying a parenthetical or a compound condition.

- A longer setup sentence followed by a short, flat one is a real and frequent pattern, often with the short sentence delivering a hard number or the verdict: "The team responded rapidly to resolve the issue as soon as it came to light. It took less than 2 hours from the first report until a fix was deployed and verified in production." Do this more than once per document.
- Fragments function as verdicts in lists — pros/cons lines, root causes, assessments — not in running prose: "inappropriate data items were added to API response representations." No subject, no article, and that's the point.
- Put the claim at the front of the sentence, same as the paragraph. Never build up to it.
- Emphasis comes from placement, brevity, and bolded keywords (§7) — never from stacked adjectives.

## 4. Paragraphs

Short: 1–3 sentences is typical, and a single-sentence paragraph is the default shape for a decision, a definition, or a load-bearing constraint — not an exception.

- Open with the claim. No transition sentence, no "to understand this, first consider..."
- A single elliptical sentence with the subject dropped can be the entire opening: "Tracks and provides access to the progress and status of asynchronous jobs." — the subject (the service) is implied, not stated.
- A concession that belongs to the paragraph's claim gets its own sentence immediately after, not folded in with "but" or "although": "This field is an implementation detail, not part of the domain or message model, and wasn't intended to be exposed in the API." Even there, note the concession rides in the same sentence via "and" — that's the ceiling, not a three-clause pileup.
- Past about five sentences, it wants a header.

## 5. Structure and argument

- Open cold on the problem, the decision, or the definition. No background section before the reader knows what's being decided or defined.
- For any decision with real alternatives, use the fixed shape (§9, Decision records) instead of inventing a new skeleton per document. State the decision before defending it.
- Ground every rule in one concrete example from an actual system — a real field name, a real client, a real incident — never a generic placeholder ("Foo," "widget").
- State the alternative or the counterargument accurately and briefly, then answer it. The Pros/Cons list is this instinct formalized: what's genuinely good about the option you're rejecting, then what it costs.
- One idea per section. Headers do real work: lowercase noun phrases for reference material ("naming," "functional mindset"), full lowercase imperative sentences when the header states the rule itself ("properties are required or nullable"), Title Case reserved for the fixed decision-record labels (Issue, Decision, Background, Options, Metadata).
- Output heuristics and name them as such when that's what they are — a rule of thumb, not a law.
- Trade-offs are the default frame. Every option gets a cost, not just a benefit.

## 6. Hedging and certainty

Firmness is marked lexically and structurally, not with adverbs.

- Bolded RFC-2119 keywords (**MUST**, **MUST NOT**, **SHOULD**, **MAY**) mark a hard requirement. Cite the convention once if the document is formal enough to need it.
- Quantifier choice does the rest of the work: "all," "any," "every" for a hard rule; "most," "usually" for a guideline with acknowledged slack. That's the hedge — not an adverb bolted onto the sentence.
- A genuinely open question gets its own line: a bullet under "Questions," a metadata field set to "TBD" or "Status: open." It does not get a hedge word smeared into the sentence that raised it.
- Hedging adverbs — "arguably," "somewhat," "potentially," "generally" as a softener — are at zero. A plain frequency word ("often," "usually") is fine when it's descriptive rather than a hedge: "it is often safer and clearer to store timezone information alongside these values" is a claim about the world, not doubt about the claim.
- Genuinely unsure and nowhere structural to put it? Say so flatly in one sentence and move on. Don't spread the uncertainty across the paragraph.

## 7. Lists, tables, and mechanics

- Lists are fragments more often than sentences: no terminal punctuation on a single-clause item, a period only once an item runs multiple clauses. No bolded lead-in labels inside a list item.
- API/reference field entries follow `fieldName (type, constraint) - description.` — a hyphen, not a colon.
- Nesting is fine for genuine sub-detail (a cost breakdown under a Cons bullet); flat is the default.
- Em dashes pair with a mid-sentence clarification — "they are not inherently dereferenceable – that is, you cannot retrieve a representation of the identified resource using just the KRN –" — and are the exception, not the reflex. Plain parentheses cover most asides.
- Semicolons join two short parallel or contrastive clauses. Never to introduce a list.
- Colons introduce an example, a quoted literal, or a code block, and pair with bold to label a section inline: **Requirement:**, **Decision:**.
- Bold marks a defined term on first use and RFC-2119 keywords — not general emphasis. If a sentence needs bold to land, shorten the sentence instead.
- Italics mark a term under active definition or a negation ("_not_ part of the domain model"), never shouting.
- Inline code for every field, endpoint, topic, and header name. A fenced example beats a paragraph describing the same shape. A formal grammar (ABNF/EBNF) beats prose when a string format has to be pinned down exactly.
- Don't chase typo-free polish for its own sake — small typos survive in the real corpus because getting the decision or the spec right is what matters. That's license to move fast, not license to be wrong.

## 8. Openings and closings

Open cold: the definition, the decision, or the broken behavior, in the first sentence. No "this document describes," no scene-setting, no background before the stakes.

- Decision records state the decision early — right after the Issue — and never re-derive it at the end.
- Incident reports open with what happened and how fast it was fixed, as two flat sentences, the second one carrying a hard number.
- Best-practice catalogs can close on a compressed, quotable rule ("The best feature gate is the one you don't create.") — the one place an aphoristic landing is in voice for work writing.
- Most documents don't get a wrap-up sentence at all. They stop at the last substantive item — a root-cause list, a Metadata table, a "See also" — rather than manufacturing a summary paragraph. Don't add one just to have a closing.

## 9. Genre playbook

One file per artifact type. See Genre files above.

## 10. Rewrites

Genre-specific rewrites live in the genre files. One applies everywhere.

**Closing.**
> *Before:* In summary, this migration approach has some trade-offs but should work well for most cases, and we can revisit if issues come up.
>
> *After:* Add the column, backfill it, write to both, read from the new one, drop the old one.

Summary-of-a-summary gone; the procedure itself is the closing.

## 11. Not for work artifacts

These belong to the blog voice (§13) and would read as an affectation in a work document. Never in a design doc, ticket, bug report, PR, or decision record:

- First-person opinion voice ("I think," "in my experience") as the default mode.
- Aphoristic one-liner closers, except the §8 carve-out for best-practice catalogs.
- Dry humor as a structural device — parentheticals undercutting the sentence, self-deprecating asides beyond the rare case in §2.
- Personal anecdote as the grounding for a claim. Ground claims in the system instead (§5).
- Exclamation marks, rhetorical questions, or any fingerprint from the §13.9 blocklist in `references/narrative.md`.

## 12. Checklist

Run this against the draft before returning it. Fix what fails.

1. Is the system or artifact the subject of the main claims, not "I" — unless this is genuinely personal/narrative writing (§13)?
2. Opens on the decision, definition, or broken behavior — no background before the stakes?
3. Every firm rule marked by a bold keyword or an "all/any/every," not an adverb?
4. Every open question in its own line or field, not smeared into a sentence?
5. At least one long-sentence-then-short-sentence moment?
6. At least one single-sentence paragraph carrying a decision or constraint?
7. A concrete example grounds each abstract rule — a real field, client, or incident, not a placeholder?
8. Bold used only for keywords/labels, not general emphasis?
9. Hedging adverbs ("arguably," "somewhat," "potentially," "generally" as softener) at zero?
10. Matches the genre shape in the genre file for this artifact type?
11. Any sentence or paragraph deletable without losing information? Delete it.
