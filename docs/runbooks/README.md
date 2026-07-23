# Runbooks

One markdown file per course task — the full, reusable, step-by-step guide for
solving that task. Open a runbook anytime in the future and follow it start to
finish without re-figuring anything out.

## How this works

- **One file per day**, named `day-NN-short-title.md` (matches the GitHub issue
  title `[M?W?D?]`).
- Each runbook is **self-contained**: goal, prerequisites, numbered steps,
  how to verify it worked, and a gotchas section.
- When reality differs from the plan (AWS changed a screen, an extra step was
  needed), record it under **⚠️ Gotchas & Deviations** at the bottom — with a
  date — so the fix lives next to the steps it affects.

## Runbooks vs OpenSpec — which goes where

| Use a runbook (`docs/runbooks/`) | Use OpenSpec (`/opsx:propose`) |
|---|---|
| Console click-throughs, CLI steps, setup | Real code features with a spec |
| "How I did this task" | "The design + requirements for this feature" |
| Every course day | Only the build days (KB, Agent, Lambda tools) |

## Index

- [day-02-explore-bedrock-console.md](day-02-explore-bedrock-console.md) — enable Claude Haiku, use the Bedrock playground
