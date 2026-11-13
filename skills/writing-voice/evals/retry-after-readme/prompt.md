---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write a README for my elixir library `retry_after`. it wraps a function and retries it when it raises or returns {:error, _}, with exponential backoff. API: `RetryAfter.run(fun, attempts: 5, base_delay: 100)` (those are the defaults). if every attempt fails it returns the last error. if the error is a %Req.Response{} with status 429 or 503 it waits for the Retry-After header instead of the backoff delay. install from hex as {:retry_after, "~> 0.1"}. MIT license. i built it over a weekend because our http client kept getting rate limited by a vendor api and i was tired of copy pasting retry loops. save it as README.md
