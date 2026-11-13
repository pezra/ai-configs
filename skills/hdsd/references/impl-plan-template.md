# Implementation plan template

Use this structure for `.plan/<slug>/impl-plan.md`. The plan is the input for implementation subagents that start cold, so each step has to make sense to someone who has read design.md, this plan, and nothing else.

Write good steps:
- **Small and independently verifiable.** After each step the build passes and the tests are green. If a step can't be verified on its own, merge it with its neighbor.
- **Test-first where practical.** Within a step, write or adjust the failing test before the code.
- **Concrete.** Name files, functions and types. "Update the handler" is too vague; "Add `validateQuota()` to `src/billing/quota.ts` and call it from `createInvoice()`" is right.
- **Ordered by dependency.** Put risky or uncertain work early, so surprises show up before much has been built on top of them.

```markdown
# Implementation plan: <Change title>

Status: draft | approved (<date>)
Design: ./design.md
Workspace: <repo-root>/.workspaces/<slug>
Branch: <branch name>
Base commit: <sha from Phase 0>; Phase 9 reviews the diff from here

## Overview
Two or three sentences on the approach and the order of the steps.

## Steps

### Step 1: <short title>
- [ ] Done
- **Goal:** what this step accomplishes.
- **Files:** `path/a`, `path/b` (new)
- **Changes:** specific edits.
- **Tests:** tests to add or update, and the command that runs them.
- **Verification:** how to confirm it worked: commands and expected output.
- **Complexity / risk:** low | medium | high, with a one-line reason.
- **Model:** sonnet | opus | haiku (see the model selection table in SKILL.md)
- **Effort:** low | medium | high (same table)
- **Depends on:** none | Step N

### Step 2: ...

## Final verification
How to check the whole change against design.md's acceptance criteria.

## Rollback
How to back the change out if it goes wrong after merging.

## Execution log
(Filled in during implementation: one line per step with its result, commit sha if any, and any deviation from the plan.)
```
