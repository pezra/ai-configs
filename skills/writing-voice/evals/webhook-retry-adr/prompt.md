---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write an ADR for confluence: should failed outbound webhook deliveries be retried by the sending service or pushed to a dead letter queue for consumers to replay? options: 1) sender retries with exponential backoff for up to 24h, 2) DLQ plus a replay endpoint, 3) both. we picked 1. pros of 2: consumers control timing, no stuck sender. cons of 2: every consumer has to build replay tooling, and we have about 30 consumers. open question: whether 24h is long enough for partners with weekend maintenance windows. save it as adr.md
