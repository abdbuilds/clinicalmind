# ClinicalMind — Architecture Decisions

This file records the *why* behind design choices. It grows as the project grows.

## System overview

```
Synthea → S3 (FHIR JSON + guidelines)
                 │                 │
                 ▼                 ▼
          Glue ETL → Athena   Bedrock Knowledge Base (RAG)
                 │                 │
                 └──────► Bedrock Agent ◄── Lambda tools
                                │            (patient summary,
                          Guardrails          drug interactions,
                         (PHI masking)         clinical query)
                                │
                                ▼
                    Cited answer with PHI masked
```

## Decisions

### 1. Anthropic API vs Amazon Bedrock → **Bedrock**
- **Context:** Claude is reachable two ways — Anthropic's API directly, or through Amazon Bedrock. Which should ClinicalMind use?
- **Decision:** Amazon Bedrock.
- **Why:**
  - **Compliance:** Bedrock is HIPAA-eligible (with a BAA) and runs inside our AWS account boundary; the Anthropic direct API is not set up for that here. ClinicalMind handles patient-shaped data, so this is decisive.
  - **Governance:** Bedrock uses AWS IAM (roles, least-privilege) + CloudTrail audit + Guardrails — enterprise controls we want.
  - **Ecosystem:** Knowledge Bases, Agents, and Guardrails are native to Bedrock — the whole project is built on them.
  - **Auth/billing:** one AWS identity + one AWS bill, no separate API key to manage.
  - **Trade-off:** Bedrock latency can be slightly higher (extra AWS routing), and it sometimes lags Anthropic on brand-new features. Acceptable for us.
  - _Use the Anthropic direct API instead for personal projects/prototypes where simplicity beats compliance._
- **Evidence:** `scripts/compare_apis.py` sends the same prompt to both. Bedrock (Haiku 4.5): ~2.6s, 30 in / 138 out tokens.

### 2. Implementation language → **Python only** (infra via CDK in Python)
- **Context:** The course mixes Python and TypeScript (and CDK in TS). The developer works in Python.
- **Decision:** All application code in **Python**. Infrastructure-as-code via **AWS CDK in Python** (`aws-cdk-lib`), not TypeScript.
- **Why:** One language to maintain; matches the developer's strength. CDK-Python keeps proper infra-as-code (clean deploy/destroy) while writing zero JavaScript.
- **Trade-off:** The `cdk` CLI still runs on Node under the hood (unavoidable), but we never write JS. Day 4's `hello_bedrock.ts` is kept as a historical artifact only.

<!-- Template for each decision:
### <short title>
- **Context:** what problem / choice
- **Decision:** what we chose
- **Why:** reasoning and trade-offs
-->
