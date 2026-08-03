# Day 03 — First Bedrock API Call in Python

**Course position:** Month 1 · Week 1 · Day 3
**GitHub issue:** #3
**Goal (plain):** Write a small Python script that asks Claude Haiku 4.5 a question via Bedrock and prints the answer.
**Definition of done:** `python3 scripts/hello_bedrock.py` prints a coherent answer about FHIR resources, from Claude Haiku 4.5.

---

## Concepts (simple + examples)

**boto3** — Python's library for AWS. One import, every service.
*Example:* `boto3.client("bedrock-runtime")` = a phone line to the AI models.

**`bedrock-runtime`** — the client for *calling* models (running them). (Different from `bedrock` = manage, and `bedrock-agent-runtime` = talk to agents.)

**Request body** — Claude on Bedrock uses Anthropic's Messages format wrapped with `anthropic_version`: a `messages` list + `max_tokens`.

**Credentials** — come automatically from `aws configure` (Day 1). Never hard-code keys.

**Response** — JSON; the text is in `content[]`, exact counts in `usage`.

---

## Prerequisites

- [ ] `.venv` exists with boto3 (`pip install -r requirements.txt`)
- [ ] AWS CLI works (`aws sts get-caller-identity`)
- [ ] Claude Haiku 4.5 usable (opened once in the playground — Day 2)

---

## Steps

1. Ensure boto3 is installed: `./.venv/bin/pip install -r requirements.txt`
2. Confirm the exact model id for Claude Haiku 4.5 in this account:
   ```bash
   aws bedrock list-inference-profiles --region us-east-1 \
     --query "inferenceProfileSummaries[?contains(inferenceProfileId,'haiku-4')].inferenceProfileId" --output text
   ```
   → use `us.anthropic.claude-haiku-4-5-20251001-v1:0`
3. Write `scripts/hello_bedrock.py` (boto3 `bedrock-runtime` → `invoke_model`).
4. Run it:
   ```bash
   source .venv/bin/activate
   python3 scripts/hello_bedrock.py
   ```

---

## Verify it worked

- [ ] The script prints a coherent answer listing FHIR R4 resources (Patient, Encounter, Observation, Condition, Medication…)
- [ ] It prints exact input/output token counts

---

## ⚠️ Gotchas & Deviations

- **2026-07-24 — Claude 4.x needs an inference-profile id, not the bare model id.**
  `invoke_model` with `anthropic.claude-haiku-4-5-20251001-v1:0` (bare) fails —
  on-demand throughput isn't supported for these models. Use the cross-region
  profile id **`us.anthropic.claude-haiku-4-5-20251001-v1:0`** (the `us.` prefix).
  Find valid ids with `aws bedrock list-inference-profiles`. Stored in
  `.env.example` as `BEDROCK_MODEL_ID`.
- Verified working 2026-07-24: input 28 / output 380 tokens on the FHIR question.
