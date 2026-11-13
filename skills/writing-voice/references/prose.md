# Prose: blog posts, essays, messages

For everything except repo writing. Numbers were measured on the 40 essays of 250+ words from 2009 on. Read `exemplars-prose.md` before writing anything longer than a few sentences, because examples carry the rhythm better than rules do.

## Stance

- **Takes a position early.** In an argument, the position is the first or second sentence, before any background: "Any integration database confers legacy status on all modules that access it." "I fall squarely on the side of not using databases as integration vectors." No throat-clearing, warm-up concession or both-sides survey first; concessions come after.
- **Earns it, then concedes what's true.** Disagreement targets the idea, with credit given: "...Mr Beust is generally correct." Sections often turn on "However," or "Unfortunately,".
- **Thinks in costs and trade offs.** "worth the cost", "more trouble than it is worth", "Engineering is all about trade offs." Usually the cost is later: evolvability, coupling, cognitive load, cost of change.
- **Scopes confidence honestly.** "i suspect", "in my experience", "This is just a rule of thumb." At most one real hedge per claim, none when Peter is sure.
- **Writes to a peer.** "you" and "we", assumes technical literacy, explains the concept but never the obvious.
- **Recurring leanings** (old, and may have changed): incrementalism, small pieces loosely joined, evolvability, human readability, evidence before optimizing, skepticism of heavy tooling and schemas, ship the 80% solution and keep improving it.

## Mechanics

| Habit | Target |
|---|---|
| Sentences | median 15 words, mean 17. ~6% are ≤6 words, ~7% reach 30. Short sentences are occasional, never staccato runs |
| Paragraphs | median 3 sentences; prose carries the argument |
| Parentheses | ~3 per 1,000 words, the main aside device: "(it was review season yet again)" |
| Dashes | ~1 per 1,000 words, spaced en dash ( – ), usually paired around an aside |
| Semicolons | ~1 per 2,000 words |
| Exclamations | nearly none in essays; fine in short personal posts |
| Questions | 1–2 per 1,000 words, real ones the next sentence answers: "How small is too small?" |
| Contractions | mixed: "do not" for weight, "don't" for ease |
| Words | "trade offs" (two words), "etc", "e.g."; degree adverbs (quite, rather, pretty, really, fairly) are fine |
| Emphasis | rarely one word in italics or bold ("will *always*"); one bold takeaway sentence allowed in a long post |

### Characteristic moves

One or two per 500 words, only where they do real work; more turns voice into parody. These show the kind of thing, not a stock to borrow from: write fresh asides rather than reusing "c'est la vie" or "mere mortals", and reuse a coinage like "The One True Schema" only for that same idea.

- `(read: ...)` when there's a real gap between the polite word and the true one: "the costs of change (read: improvement)"
- Inline `a) ... b) ...` lists, only when the items are short
- Scare quotes that do work: “efforts”, “documentation”
- Footnotes for tangents and caveats
- A dry fragment as verdict: "A losing proposition if there ever was one."
- Wry understatement and self-deprecation: "my readers (all three of you)", "totally hypothetically"
- A capitalized name for a bad pattern: "The One True Schema"
- A casual word in formal reasoning: "it really sucks", "squishy", "no sweat"
- Short, plain or playful headings: "Maybe Monogamy", "Pardon me while i digress…", "Back on point"
- Concrete, mundane examples: an invoice with line items, a radio only available with one trim package
- Open credit to sources: "Shamelessly copied from Chris Wanstrath."
- "Mr Lastname" for people in a technical argument after first mention; first names for friends

## Shape

**Openings** go straight to the claim, situation or trigger, and an argument states its position there rather than in paragraph 2: "One of the hardest won lessons of my career is the power of incrementalism." Never announce what the post will discuss.

**Middles** set up the problem concretely, name the appeal of the wrong answer ("This approach is very appealing."), show why it fails with an example or code, then give the alternative with its costs. Long posts use plain headings, often a handful of named items with a section each.

**Endings** stop when done, on a practical consequence, a plain recommendation, a real question, or what happens next: "I'll let you know how it works out." No inspirational closer or grander restatement. A short plain "Conclusion" is fine in a long how-to.

## Registers

| Register | How it changes |
|---|---|
| Technical essay | Full voice: sections, examples, footnotes, firm opinion |
| Response to someone | Names and links them, restates their argument fairly, disagrees point by point |
| How-to or war story | Chronological, problem first, command output and config included, lighter on opinion |
| Personal or travel | Simple past, short, warm, understated; names people; no moral |
| Short post or social | One or two plain, dry sentences: "So far i am underwhelmed." |
| Team message or email | Inferred (no blog examples): position first, a few sentences of reasoning, a clear ask. Short; lowercase i and dry tone carry the voice. A direct question can open instead of a claim. A salutation takes a comma and its own line ("Team,") |

When de-AI-ing Peter's draft, keep Peter's content and position; change the phrasing, not the claims.

## Don't copy

- **Typos and slips** in the exemplars' sources ("it's" for "its", "suppose to", dropped words). Write correctly. Informal choices are voice: starting with "So", "And" or "But", fragments, "trade offs".
- **2005–2008 habits** unless asked: capital "I", longer, more combative. Useful for stance, not as the model.

## Extra checks

1. Read for rhythm: merge runs of short sentences and flatten paragraphs that all end on a zinger.
2. For an argument, confirm the position is in the first two sentences and that it says something Peter would have to defend.
