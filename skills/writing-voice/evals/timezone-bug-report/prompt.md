---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write a jira bug report: the billing statement PDF shows due dates one day early for customers in Pacific time. repro: create an account with tz America/Los_Angeles, set due date 2026-03-15, generate statement, PDF says March 14. API returns dueDate 2026-03-15 correctly. i think the PDF renderer converts the date to UTC midnight then formats in local time but i havent confirmed. affects all west-of-UTC customers probably. save as bug.md
