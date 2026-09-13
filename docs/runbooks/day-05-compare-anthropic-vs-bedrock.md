# Day 05 — Compare Anthropic API vs Bedrock API

**Course position:** Month 1 · Week 1 · Day 5
**GitHub issue:** #5
**Goal (plain):** Send the same prompt to Claude Haiku 4.5 via both the Anthropic API and Bedrock, compare them, and write the decision in ARCHITECTURE.md.
**Definition of done:** Script runs and prints results; ARCHITECTURE.md explains why ClinicalMind uses Bedrock.

---

## The comparison (concept)

| | Anthropic API (direct) | Amazon Bedrock |
|---|---|---|
| Auth | API key `sk-ant-…` | AWS IAM (`~/.aws` / roles) |
| Billing | Separate Anthropic account | Your AWS bill |
| Runs | Anthropic's servers | Inside your AWS boundary |
| HIPAA | Not set up here | HIPAA-eligible (with BAA) |
| Governance | Basic | IAM + CloudTrail + Guardrails |
| Ecosystem | Newest features first | KB / Agents / Guardrails native |
| Best for | Prototypes | Enterprise, patient data |

**Decision → Bedrock** for ClinicalMind (compliance + governance + native KB/Agents/Guardrails). Full rationale in `ARCHITECTURE.md`.

---

## Steps

1. `./.venv/bin/pip install -r requirements.txt` (adds `anthropic`).
2. Write `scripts/compare_apis.py` — same prompt to both; Bedrock always runs, Anthropic runs only if `ANTHROPIC_API_KEY` is set. Time each call, print latency + tokens.
3. Run:
   ```bash
   source .venv/bin/activate
   python3 scripts/compare_apis.py
   ```
4. Write the Anthropic-vs-Bedrock decision in `ARCHITECTURE.md`.

---

## Verify it worked

- [ ] Script prints the Bedrock answer + latency + tokens
- [ ] (If a key is set) prints the Anthropic answer too; otherwise skips cleanly
- [ ] `ARCHITECTURE.md` has the decision written out

---

## ⚠️ Gotchas & Deviations

- **2026-08-04 — No Anthropic API key on hand.** Day 5 normally calls the
  Anthropic API directly, which needs a separate `ANTHROPIC_API_KEY` (own signup
  + credit). To keep momentum we made the Anthropic call **optional**: the script
  auto-skips it if no key is set, and we captured the comparison in ARCHITECTURE.md
  from the (live) Bedrock side + known differences. Add a key and rerun to see
  both live. Bedrock side verified: ~2.6s, 30 in / 138 out tokens.
- **2026-08-04 — Project is now Python-only.** Day 4's TypeScript is kept as
  history; no new Node code. Infra later = CDK in Python. See ARCHITECTURE.md §2.
- Model ids: Bedrock uses `us.anthropic.claude-haiku-4-5-20251001-v1:0`;
  the Anthropic direct API uses the plain alias `claude-haiku-4-5`.
