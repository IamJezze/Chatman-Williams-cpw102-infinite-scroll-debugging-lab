# Incident Note — INC-204

**Responders:**

## Investigation log

Record **every debugging step in chronological order as you work**, including unsuccessful attempts and changes you undo. Commit your work as you go. 

For each step, briefly note what you tried and why, what you observed, and what you concluded or decided to try next.

Include relevant inputs, code changes, or output so someone else can follow your investigation. 

Use numbered entries or timestamps. Use Markdown formatting to make it easy to read.

Nov 4th 2026 @ 1342 - Noticed page variable was not incrementing, causing only the first page to be loaded repeatedly

Nov 4th 2026 @ 1402 - Added message to ask user to enter valid input, still moves on feed regardless

Nov 4th 2026 @ 1420 - Added check for if all posts have been displayed

## Resolution

Explain the causes, your repairs, and the evidence that verifies them. Identify
anything still uncertain or unresolved. Make code changes in `feed.py`.
