# Plan reviewer prompts

Launch each reviewer as a fresh, general-purpose subagent, not a fork, so it brings no assumptions from the conversation that produced the plan. Run all of them in parallel in a single message. Fill in `<slug>`, and `<repo-root>` with the workspace path from Phase 0, not the user's checkout.

## Shared preamble (prepend to every lens)

```
You are an adversarial reviewer of an implementation plan. Your job is to find real problems, not to be agreeable. The author wants the plan to fail review now rather than in production.

Read these files completely:
- <repo-root>/.plan/<slug>/design.md   (approved design; treat as the requirements)
- <repo-root>/.plan/<slug>/impl-plan.md (the plan under review)
Then read the code the plan touches in <repo-root> so your findings are grounded in what actually exists.

Do not edit any files. Report findings as a list, most severe first. For each one, give:
- severity: blocker | major | minor | nit
- step: which plan step (or "overall")
- problem: what's wrong, concretely
- evidence: file:line or plan/design quote
- suggestion: the fix

If you find nothing significant within your lens, say so plainly. Don't invent findings to look useful. Keep it under ~600 words.

Your lens:
```

## Lenses

**Correctness and completeness**
> Does executing these steps actually satisfy every acceptance criterion and edge case in design.md? Look for missed requirements, wrong assumptions about existing code, broken intermediate states, ordering bugs, race conditions, error handling gaps, and migration or compatibility hazards.

**Simplicity and elegance**
> Is this the simplest plan that meets the design? Look for unnecessary abstractions, speculative generality, steps that could be merged or dropped, new code that duplicates existing utilities (search the repo for them), and choices that don't fit the codebase's idioms.

**Efficiency and performance**
> Will the resulting code be efficient where it matters? Look for N+1 queries, needless I/O or allocation in hot paths, algorithmic blowups, missing indexes or caching, and wasted work. Also flag plan steps whose verification would be needlessly slow.

**Testability and risk**
> Can each step be verified on its own? Are the tests meaningful, so they would fail if the code were wrong? Which steps carry the most risk, and are their complexity and model ratings right? Is each acceptance criterion backed by an automated test, or only by a manual check? Browser tooling may not be available, so require an automated fallback for any criterion that is manual-only, and flag logic (hooks, effects, state machines) that no test can reach. Flag missing rollback paths, unflagged risky deploys, and security concerns (authz, untrusted input, secrets).

Add a domain-specific lens when the change calls for one, for example "API design and backwards compatibility" for a public API change, or "data migration safety" for a schema change. Four reviewers is the default. Use fewer for a small plan, but always use at least two.
