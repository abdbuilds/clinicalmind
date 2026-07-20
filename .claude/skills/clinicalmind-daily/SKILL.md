---
name: clinicalmind-daily
description: Run one day of the ClinicalMind course end-to-end. Use when the user says they are on a given Month/Week/Day (e.g. "I'm on Month 1 Week 2 Day 3") or asks to start/continue today's ClinicalMind session.
metadata:
  author: abdulrehman
  version: "1.0"
---

Run a single ClinicalMind course day from start to committed result.

## Communication rule (always)
Explain everything in very simple, plain language and give a concrete example wherever possible. The user is learning; do not assume jargon is understood.

## Steps

1. **Locate the day.** Read the relevant section of `CLINICALMIND_MASTER.md` for the stated Month/Week/Day. Restate today's Goal and Definition of Done in one or two plain sentences.

2. **Open the issue.** Find the matching GitHub issue (title starts with `[M?W?D?]`): `gh issue list --state open`. If none exists, create it from the `Course Day` template. Mark it in progress.

3. **Teach first, then build.** Before writing code, explain the concepts for the day simply, with examples. Confirm the user understands.

4. **Decide the workflow:**
   - Trivial/mechanical task (scaffold, config, single script) → build directly.
   - Real feature (a Lambda tool, the Agent, the KB, ETL job) → run `/opsx:propose "<feature>"` first, review the spec together, then `/opsx:apply` to build.

5. **Build** the day's deliverables exactly as the course specifies.

6. **Verify the Definition of Done.** Actually run the check (script output, `aws` call, file exists). Show the real result — never claim done without observing it.

7. **Commit + push.** One day = one committed result. Use a conventional commit message. End the message with the required Co-Authored-By line.

8. **Close the issue** with a short comment linking the commit(s). If it's the last day of a week, create the git tag the course asks for (e.g. `week-1-complete`).

## Rules that must never be broken
- Never advance to the next day until the current Definition of Done is met.
- Every coding day ends with a commit — no exceptions.
- If something breaks, fix it before moving on.
- Secrets go only in `.env` (git-ignored), never hardcoded.
- All patient data is synthetic (Synthea) — never real PHI.
