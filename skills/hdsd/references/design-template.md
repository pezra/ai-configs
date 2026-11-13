# Design doc template

Use this structure for `.plan/<slug>/design.md`. Leave out a section only when it truly doesn't apply, and say so in one line ("No data migration needed") rather than deleting it silently. That way the reader can tell the question was considered.

```markdown
# <Change title>

Status: draft | approved (<date>)
Type: feature | bug

## Problem
What's wrong or missing, and who it hurts. For a bug: observed vs. expected behavior, repro steps, and the suspected or confirmed root cause.

## Goals
- Concrete outcomes this change delivers.

## Non-goals
- Things a reasonable person might expect this change to do that it deliberately won't.

## Acceptance criteria
- [ ] Observable, testable statements. Each one should map to at least one test or a manual check.

## Current state
The relevant code as it is today: files, modules, data flow. Cite `path:line`.

## Proposed design
How the change works. Include interfaces, data shapes, control flow, and the reasons behind the key choices.

## Alternatives considered
- <Option>: why it was rejected.

## Edge cases and failure modes
- Input or state → expected behavior.

## Compatibility, migration and rollout
API or schema changes, data migration, feature flags, backwards compatibility, deploy order.

## Security, performance and observability
Only what's relevant: authz, untrusted input, hot paths, logging and metrics.

## Testing strategy
What gets unit, integration and manual testing, and which existing tests change.

## Open questions
- Anything unresolved. All of these must be closed before the doc is approved.
```
