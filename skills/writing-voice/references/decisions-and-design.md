# Decision records and design docs

## 9. Genre playbook (excerpt)

**Decision records.** The default shape for any decision with real alternatives: `Issue` (the problem, one or two sentences) → `Decision` (stated flat, sometimes one fragment: "Default to old behavior (option 1)") → `Background` (Assumptions / Questions, bulleted) → `Options`, numbered, each carrying `Pros` / `Cons` / `Cost` fragment-lists → a closing `Metadata` table (Status, Impact, Driver, Contributors, Due date).

**Design docs / RFCs.** Open with the definition or problem in one flat sentence. RFC-2119 bold keywords for requirements (§6). One concrete, real-system example per abstract rule. Exhaustive or formal material — grammars, edge-case tables — goes in an appendix rather than bloating the main argument.

## 10. Rewrites (excerpt)

**Vague framing → stated decision.**
> *Before:* There are a few different ways we could handle this, and there are trade-offs either way, but I wanted to lay out some options for discussion.
>
> *After:* Default to old behavior (option 1). New clients can opt into the new behavior with a header; nobody's existing integration breaks.

Decision stated before the options, not after. No meta-commentary about there being a discussion to have.

**Hedged claim → firm rule, uncertainty isolated.**
> *Before:* It's probably generally a good idea for services to usually notify the relationship tracker when relationships change, though there might be some cases where that's not needed.
>
> *After:* Services **MUST** notify the relationship tracker when relationships change.
>
> Open question: does this apply to relationships created by a bulk import? Not yet decided.

The rule is unhedged and marked with the RFC-2119 keyword; the real uncertainty moves to its own line instead of softening the rule.
