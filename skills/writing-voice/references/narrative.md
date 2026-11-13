# 13. Personal and narrative writing (secondary register)

The core file (`SKILL.md`, §§1–12) is the default. This file is for the rare case of an actual blog post or personal essay — narrative, opinion, or first-person technical writing meant to stand alone, not something a colleague has to act on. Where this file conflicts with §§1–12, this file governs, but only for that kind of writing.

### 13.1 Voice

A working engineer talking to a peer at a whiteboard, usually after having made the mistake once. Flat declarative claims, no warm-up, no apology. Confidence earned, not performed. Humor is deadpan and lives in parentheses and in short sentences following long ones. The piece stops the moment the point is made.

### 13.2 Sentences and paragraphs

Baseline, measured from a 15-post sample: technical prose median ~20 words, band 14–30, range 4–62; ~1 in 8 under 10 words, ~1 in 10 over 40. Narrative prose runs shorter: median ~13, band 8–20. Paragraphs run 1–6 sentences, median 2; roughly 35–40% are a single sentence.

- One main clause plus one qualifier — a claim and its condition. No three-clause pileups.
- Follow a long sentence with a short one, repeatedly — the single most characteristic rhythm.
- Fragments only as verdicts ("Not true."), one or two per piece. Never for atmosphere.
- Semicolons join two independent clauses, 4–8 per 1,000 words. Never to introduce a list.
- One-sentence paragraphs are a structural tool: a rule of thumb, an unburiable caveat, a pivot, a verdict. 3–6 per 1,000 words.
- Turn inside the paragraph: assertion → mechanism or example → concession, concession last and short.
- Over ~6 sentences, it wants a header.

### 13.3 The reader and argument

A peer of equal competence who has not thought about this particular thing yet. Never a student.

- Pick one person-mode and hold it: *opinion* = heavy first person, almost no "you"; *how-to* = heavy second person plus imperatives; *reference* = neither, pure present-tense declarative.
- "We" means "our company/profession/community" only. Never fake-inclusive, never royal.
- Thesis in the first paragraph, restated compressed at the end. Nothing withheld for a reveal.
- Ground the claim in first-hand experience immediately: "here is what happened when I tried it," not citation or authority.
- Concessions get their own sentence, then move on. Acknowledged, not litigated.
- State the counterargument accurately and briefly, answer it in one or two sentences. "Not true, because X" is in voice.
- Output heuristics, not frameworks, and label them as heuristics. Trade-offs are the default frame.

### 13.4 Register and humor

Plainspoken professional. No slang, no corporate abstraction. Contractions ~1 per 3–4 sentences, with occasional uncontracted "do not" for weight.

- Humor is dry, brief, structurally subordinate — a parenthetical, a trailing clause, or a short sentence after a serious one. Never the point of a paragraph.
- Understatement and the flat aside that undercuts its own sentence are the reliable forms.
- Self-deprecation targets temperament and process, never competence. "I'm no expert, but…" is out.
- Blunt about artifacts and ideas; fair to people.
- Exclamation marks: 0–2 per piece, genuine delight only. No hype vocabulary ("game-changer," "leverage," "10x").

### 13.5 Opinion and uncertainty

Assertions are unhedged; uncertainty is stated separately in its own sentence.

- Assert flatly. "You should be using it." Owning the opinion in first person *is* the hedge.
- Name what you're uncertain about, briefly. One clean admission beats five softening adverbs.
- Scope rather than weaken: not "this might sometimes work" but "this is right when X, wrong when Y."
- Admit past error as narrative, not apology: "Once I thought X. Then I tried it. Now I don't."
- Never hedge the closing sentence.

### 13.6 Openings and closings

Openings are cold, 9–20 words: flat declarative thesis, personal reversal or recurring annoyance, bare fact, or naming the interlocutor. Never a definition, a scene, a statistic, or "in this post."

Closings land, they don't summarize. Last sentence runs 40–70% of the post's median length, often under 12 words: compressed thesis, aphoristic widening one-liner, or a practical caveat naming where the advice fails. No call to action, no "hope this helps." Stop on the beat.

### 13.7 Mechanics

Per ~1,000 words, measured from the sample:

| Feature | Rate | Use |
|---|---|---|
| Em dashes | 3–7 | Apposition, mid-sentence emphasis. Not a comma substitute. |
| Semicolons | 4–8 | Joining related independent clauses. |
| Colons | 5–11 | Introducing examples, lists, code. |
| Parentheticals | 4–9 | Asides, caveats, dry jokes. |
| Question marks | 1–2 | A section header or one genuine pivot. |
| Exclamation marks | 0–2 | Genuine enthusiasm only. |
| Bold | 0 | Essentially never. |
| Italics | 0–12 | Terms under discussion, paired values. Never shouting. |

Lists are 3–6 short parallel fragments, no terminal punctuation, no nesting. Headers are lowercase or sentence case, never Title Case, never numbered. No horizontal rules, callout boxes, emoji, tables of contents, or bolded "TL;DR."

### 13.8 Rewrites

**Opening.**
> *Before:* In this post, I'd like to explore the topic of feature flags and share a few thoughts on why they can be something of a double-edged sword.
>
> *After:* Feature flags are technical debt with a friendly face. Every one you add is a branch in your program that you have quietly promised to keep testing, and most teams never make good on the promise. I have deleted far more dead flags than I have shipped live ones.

**Hedged claim → asserted claim with a real hedge attached.**
> *Before:* It could perhaps be argued that retry logic is somewhat overused, and that under certain circumstances it may potentially make outages worse.
>
> *After:* Retries make outages worse more often than they help. A service that is already falling over does not need three times its normal traffic.
>
> I am not saying never retry. I am saying a retry needs a budget and a breaker, and almost nobody writes those parts.

**Counterargument.**
> *Before:* Of course, some readers may disagree, and there are legitimate arguments on both sides. Advocates of the monorepo approach would point to a number of genuine benefits, and those benefits are real, although on balance I come down on the other side.
>
> *After:* The usual objection is that a monorepo makes cross-cutting changes trivial. True, and worth something.
>
> But it buys you cheap edits to code that should not have been coupled in the first place, and the bill shows up later with interest. I would rather pay the smaller bill now.
>
> Reasonable people land the other way on this. I have been on teams where they were right.

### 13.9 Do not imitate

This blocklist applies to personal and narrative writing only. Work artifacts have their own conventions (§7, §9).

These are the author's fingerprints. Reproducing them is impersonation, and reads as a costume.

- Lowercase "i" as the first-person pronoun. Use standard capitalization.
- Uncorrected typos in published prose.
- "What could possibly go wrong?" — the site tagline, not prose. Never use it as a line, header, or closer.
- The Agile-Manifesto pastiche ("X over Y" value pairs, then "I value the things on the right, but the things on the left more"). Borrowed structure; do not reuse.
- Jokey appendix headers ("Appendix A: Wherein I get sorta mathy about…").
- Observed set-phrase closers: "In short, it is killer." / "Easy as pie." / "c'est la vie" / "3 yards and a cloud of dust" / "No monolith lasts forever." / "So many stars." Write your own.
- Recurring topics: REST/HATEOAS/hypermedia/content negotiation; schema languages as personal grievance; Roy Fielding, *The Pragmatic Programmer*, the Agile Manifesto as touchstones; Emacs, Ruby/Rails, Elixir/OTP, monolith decomposition; and the personal-life material (kids, Colorado skiing, Grand Canyon rafting, Denver/Atlanta/Santiago, the 2017 eclipse).
- Seniority claims ("one of the hardest-won lessons of my career," "the engineers on my team"). Grounding a claim in first-hand experience is the style; the specific biography is not yours to borrow.
- Never pad to length. If the point takes 280 words, the post is 280 words, and it does not apologize for it.

### 13.10 Checklist (narrative)

1. Thesis in the first two sentences?
2. Last sentence under 12 words and unhedged?
3. At least three one-sentence paragraphs?
4. Long sentence followed by a short one at least three times?
5. Every concession its own sentence?
6. Bold used zero times?
7. Hedging adverbs at zero?

---

Derived primarily from ~40 Confluence pages authored 2023–2026 across the Platform Guidelines, Shared Services, Accounts Team, and Idea to Production spaces — design docs, decision records, API/service specs, incident reports, and one team code-quality rubric. Most Accounts Team and Idea to Production pages were templated retro boards or unfilled interview scaffolding with no original prose; they contributed the "Working notes" genre (§9) and little else.

§13 is derived separately, from 15 posts at barelyenough.org, 2007–2022 (technical, opinion, and narrative), and governs only personal/narrative writing. The "What could possibly go wrong?" string appears on every page as the site tagline, not as body prose — see §13.9.
