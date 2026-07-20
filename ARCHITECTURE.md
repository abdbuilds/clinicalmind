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

_None recorded yet. First entry lands in Week 1 Day 5 (Anthropic API vs Bedrock)._

<!-- Template for each decision:
### <short title>
- **Context:** what problem / choice
- **Decision:** what we chose
- **Why:** reasoning and trade-offs
-->
