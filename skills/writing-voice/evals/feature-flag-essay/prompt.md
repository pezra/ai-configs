---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write a short blog post (~400 words) for barelyenough.org arguing that feature flags older than 90 days are tech debt and should be removed. my view: flags are great for rollouts, but long-lived flags multiply code paths and nobody remembers which are safe to delete. at my last job we had about 200 stale flags. recommendation: every flag gets an expiry date when it's created and CI fails once it passes. save it as post.md
