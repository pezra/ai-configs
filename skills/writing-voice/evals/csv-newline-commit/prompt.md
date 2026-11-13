---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

write a commit message for this change: CSV export was dropping rows whose description field contained a newline. the exporter split the file on \n before handling quoted fields. i replaced the hand rolled parser with NimbleCSV and added a regression test with a multi-line description. save it as commit.txt
