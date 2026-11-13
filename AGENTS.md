## Writing voice

Everything written on my behalf follows my voice guide: docs, READMEs, ADRs, design docs, Confluence pages, Jira tickets, bug reports, PR descriptions, commit messages, blog posts, Slack and email drafts, and any prose you draft in a file.

Load the `writing-voice` skill before drafting or editing any of those. Do not draft first and style after.

The core, which applies even when the skill is not loaded:

- Thesis in the first sentence. No "in this post," no background before the stakes.
- Assert flatly, then state uncertainty as its own separate sentence. Hedging adverbs ("arguably," "somewhat," "potentially," "in some sense") at zero.
- Every concession gets its own sentence, not a subordinate clause.
- Follow a long sentence with a short one. Emphasis comes from brevity, never from typography. Bold only for RFC-2119 keywords and defined terms in specs; no emoji, no callout boxes, no "TL;DR."
- Lowercase "i" mid-sentence; capital "I" only to start a sentence. No em dashes.
- Never invent experiences, opinions or results. Leave a `[Peter: ...]` slot instead.
- Show mechanism: code block, trace, or numbered procedure over another descriptive paragraph.
- Land short and unhedged. No call to action, no "hope this helps."
- If it can be shorter, it is not done.

Scope: this governs written deliverables, not your conversational replies to me in the terminal. Say "in my voice" if you want it applied to something outside that list.

## Subagents

Delegate large, mechanical, or high-output work to subagents; keep the main context for judgment, design, and talking with me.

Delegate:

- **Mechanical multi-file changes**: renames, migrations, repeated fixes, call-site updates.
- **High-output work**: test runs, builds, long logs, reading many or large files, broad searches. Return conclusions, not raw output.
- **Separable tasks**: independent feature pieces, comparing options, multi-file reviews. Run in parallel.

How:

- Use the smallest model and lowest effort that can do the job; escalate only if the task needs real reasoning or a cheaper attempt fails.
- Start fresh, not forked. Pass only what the task needs: goal, paths, constraints, conventions, definition of done.
- Ask for a short report: changes, findings, failures, anything suspicious.
- Verify before building on results: spot-check diffs, rerun tests.

Don't delegate small tasks, work needing back-and-forth with me, or design judgment calls.

