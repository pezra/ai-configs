# Work documents

Design docs, decision records, API and service references, incident reports, team standards, tickets, bug reports and working notes. Derived from about 40 of Peter's Confluence pages (2023–2026). The rules in `SKILL.md` still apply: lowercase i, nothing invented, no AI habits.

## Contents

- Voice
- Register
- Sentences and paragraphs
- Structure
- Hedging and certainty
- Mechanics
- Openings and closings
- Genres
- Rewrites
- Not for work documents
- Extra checks

## Voice

An engineer stating a decision, a spec or a fact about a system to a peer who has to act on it. Flat declarative claims, no warm-up, no apology, no hedge disguised as politeness. Confidence comes from specificity (a number, a field name, a concrete example), not from adverbs.

The governing instinct is deflation: state the rule, not a case for how carefully you considered it. Useful beats impressive. Humor, when it shows up at all, is dry, brief and subordinate, usually a parenthetical.

## Register

The system or the artifact is the subject, not "i": "A namespace is a container for related data," not "I think of a namespace as...". "This event indicates that the enclosed service agreement, account and service point exist," not "We're sending this event because...". First person essentially does not appear in specs, glossaries, decision records or rubrics.

- First person shows up in two places only. One is a self-deprecating aside: "Datafeed type `ACCOUNTDELTA` (i know, i know, this isn't account data or deltas). It's terrible but unavoidable." The other is a genuinely hedged guess inside an open question: "i'm unsure how much extra load this will put on balance and account service." Both are rare.
- "You" is a deliberate audience switch, used only when walking an external API consumer through a worked scenario: "You have a balance record in your DB. It has `syncedAt: 2025-01-20T14:30:00Z`... Check `syncedAt`." Internal specs and decision records never address "you".
- Obligations on other systems are third-person normative ("Consumers of this API **MUST** ignore unrecognized fields"), not imperative.
- "We" means the team or org making the decision ("We should move to a low-trust paradigm"), never a stand-in for "i".

## Sentences and paragraphs

Expository sentences run a median of 15–20 words; bullets, pros/cons lines and glossary entries run 5–10. A five-word sentence can sit next to a 30-word one carrying a condition.

- A longer setup sentence followed by a short flat one is frequent, often with the short one carrying a hard number or the verdict: "The team responded rapidly to resolve the issue as soon as it came to light. It took less than 2 hours from the first report until a fix was deployed and verified in production."
- Fragments work as verdicts in lists (pros/cons, root causes, assessments), not in running prose.
- Put the claim at the front of the sentence and the paragraph. Never build up to it.
- Paragraphs run 1–3 sentences. A single-sentence paragraph suits a decision, a definition or a load-bearing constraint. It is not a device for drama.
- An opening can be one elliptical sentence with the subject dropped: "Tracks and provides access to the progress and status of asynchronous jobs."
- A concession gets its own sentence right after the claim it qualifies, not a "but" or "although" clause folded in.
- Past about five sentences, a paragraph wants a heading.

## Structure

- Open cold on the problem, the decision or the definition. No background section before the reader knows what's being decided.
- State the decision before defending it.
- Ground every rule in one concrete example from a real system: a real field name, client or incident. Never "foo" or "widget". If Peter didn't supply one, leave a `[Peter: example?]` slot.
- State the alternative accurately and briefly, then answer it. Pros/cons lists formalize this: what's genuinely good about the rejected option, then what it costs.
- Every option gets a cost, not just a benefit.
- Call a heuristic a heuristic.
- One idea per section. Headings are lowercase noun phrases for reference material ("naming", "functional mindset"), or lowercase sentences when the heading states the rule ("properties are required or nullable"). Title Case only for the fixed decision-record labels.

## Hedging and certainty

Firmness is marked by keywords and structure, not adverbs.

- Bold RFC-2119 keywords (**MUST**, **MUST NOT**, **SHOULD**, **MAY**) mark requirements. Cite the convention once if the document is formal enough to need it.
- Quantifiers do the rest: "all", "any", "every" for a hard rule; "most", "usually" for a guideline with slack.
- An open question gets its own line: a bullet under "Questions", or a field set to "TBD". It does not get a hedge word smeared into the sentence that raised it.
- Hedging adverbs ("arguably", "somewhat", "potentially", "generally" as a softener) are at zero. A frequency word that describes the world is fine: "it is often safer and clearer to store timezone information alongside these values."
- Genuinely unsure with nowhere structural to put it? Say so flatly in one sentence and move on.

## Mechanics

- List items are fragments more often than sentences. No terminal punctuation on a single-clause item; a period once an item runs multiple clauses. No bolded lead-in labels.
- Field entries: `fieldName (type, constraint) - description.` with a hyphen, not a colon.
- Nesting only for genuine sub-detail, such as a cost breakdown under a Cons bullet.
- Dashes are rare and spaced en dashes ( – ), paired around a clarification. Parentheses cover most asides.
- Semicolons join two short parallel or contrasting clauses. Never to introduce a list.
- Colons introduce an example, a literal or a code block, and can label a section inline with bold: **Decision:**.
- Bold marks RFC-2119 keywords, a defined term on first use and inline section labels. Nothing else. If a sentence needs bold to land, shorten it.
- Italics mark a term under definition or a negation ("_not_ part of the domain model").
- Inline code for every field, endpoint, topic and header name. A fenced example beats a paragraph describing the same shape. A formal grammar (ABNF) beats prose when a string format must be exact.

## Openings and closings

Open on the definition, the decision or the broken behavior in the first sentence. Never "this document describes".

Most documents get no wrap-up. They stop at the last substantive item (a root-cause list, a Metadata table, a "See also") rather than a summary paragraph. The one exception is a best-practice catalog, which can close on a compressed rule: "The best feature gate is the one you don't create."

## Genres

**Decision records.** Default shape for any decision with real alternatives:

1. `Issue`: the problem in one or two sentences
2. `Decision`: stated flat, sometimes a fragment ("Default to old behavior (option 1)")
3. `Background`: Assumptions and Questions, bulleted
4. `Options`: numbered, each with Pros, Cons and Cost as fragment lists
5. `Metadata` table: Status, Impact, Driver, Contributors, Due date

The decision comes right after the Issue and is never re-derived at the end.

**Design docs and RFCs.** Open with the definition or problem in one flat sentence. RFC-2119 keywords for requirements. One real example per abstract rule. Grammars and edge-case tables go in an appendix.

**API and service references.** One field entry per field. One sentence per definition unless the term is genuinely surprising. Inline code everywhere a name appears.

**Incident reports.** Open with what happened and how fast it was fixed, as two flat sentences, the second carrying a hard number. Headings are the reader's plain questions: "what happened", "how did this happen", "root causes". Root causes are process gaps, not people, even when the chronology is specific about what broke.

**Team standards and rubrics.** State the property the finished work must have, not an instruction to the person: "all function names clearly articulate what the function does", not "name your functions clearly". Pair every good behavior with its mirrored bad one. Skip partial credit.

**Tickets and stories.** The title is a flat declarative of the outcome, not a category label. The first line says what will be true when it's done. Acceptance criteria are 3–6 short parallel fragments, not nested. Known limits get their own line: "This does not cover X." No first person.

**Bug reports.** Open with the broken behavior in one present-tense sentence, not the investigation. Then 3–6 numbered reproduction steps, expected, actual, with nothing between them. Evidence gets one colon lead-in and no narration. Separate what is known from what is suspected, in that order, and label the suspicion: "I have not confirmed the cause." Severity is flat and unhedged.

**Working notes** (meeting notes, interview notes, scratch analysis nobody else acts on). The rules relax here. A fragment can stand alone as a verdict ("high team to team variability"), a concession can trail as a clause, and one scare-quoted word ("sloppy") can stand in for a clause. Don't polish these. The compression is the point.

## Rewrites

**Vague framing to a stated decision.**

> Before: There are a few different ways we could handle this, and there are trade-offs either way, but I wanted to lay out some options for discussion.
>
> After: Default to old behavior (option 1). New clients can opt into the new behavior with a header; no existing integration breaks.

**Hedged claim to a firm rule, with the uncertainty isolated.**

> Before: It's probably generally a good idea for services to usually notify the relationship tracker when relationships change, though there might be some cases where that's not needed.
>
> After: Services **MUST** notify the relationship tracker when relationships change.
>
> Open question: does this apply to relationships created by a bulk import? Not yet decided.

**First-person narration to an impersonal spec.**

> Before: I decided that the payable amount for an account shouldn't live with the account record itself, since we already have a service that tracks balances, so I made it pull from there instead.
>
> After: Unlike invoices and other payable categories, the payable amount of an account is maintained in a separate service.

The reasoning that produced the decision isn't restated, just the result.

**Teacherly gloss to a reference entry.**

> Before: A KRN, or KUBRA Resource Name, is basically our version of a URN. It's a string that uniquely identifies a resource, kind of like a primary key but portable across services.
>
> After: A **KRN** is a name, not a locator. KRNs are not inherently dereferenceable – a representation of the identified resource cannot be retrieved using just the KRN.

**Summary closing to the procedure itself.**

> Before: In summary, this migration approach has some trade-offs but should work well for most cases, and we can revisit if issues come up.
>
> After: Add the column, backfill it, write to both, read from the new one, drop the old one.

## Not for work documents

These belong to the blog voice in `prose.md` and read as an affectation here:

- First-person opinion ("i think", "in my experience") as the default mode
- Aphoristic closers, except in a best-practice catalog
- Humor as a structural device, or self-deprecation beyond the rare aside
- Personal anecdote as grounding. Ground claims in the system
- Exclamation marks and rhetorical questions
- The characteristic moves from `prose.md` (`(read: ...)`, named bad patterns, casual words in formal reasoning)

## Extra checks

1. The system or artifact is the subject of the main claims, not "i".
2. Every firm rule carries a bold keyword or an "all/any/every", not an adverb.
3. Every open question sits on its own line or in its own field.
4. Each abstract rule has a real example or a `[Peter: ...]` slot.
5. The shape matches the genre above.
6. Delete any sentence that can go without losing information.
