# ClinicalMind — Complete AWS Bedrock Mastery & Certification Roadmap

**Owner:** Abdulrehman Saleem
**Start Date:** _______________
**Target Completion:** _______________ (3 months from start)
**Goal:** Master AWS Bedrock, build a production-grade clinical AI agent, and earn 2 AWS certifications

---

## How To Use This File

This is a single self-contained course file. It never needs to be updated.
Drop it into your project root in VS Code. Open Claude Code alongside it.

At the start of every session, tell Claude Code exactly this:

> "I am on [Month X, Week Y, Day Z] of the ClinicalMind course.
> Read CLINICALMIND_MASTER.md and guide me through today's session completely."

Claude Code will read this file, understand your exact position, know what to build, what concepts to teach, and what done looks like. You follow along and commit at the end of every day.

**Rules that must never be broken:**
- One day = one session = one committed result
- Never move to the next day until the current day's definition of done is met
- Every coding day ends with a git commit — no exceptions
- If something breaks, fix it before moving forward — do not skip
- Month 2 is study only — no coding, no skipping, no cramming

---

## What You Will Master

### AWS Core Services
- S3 — bucket creation, IAM policies, folder structure, sync commands, event triggers
- IAM — users, roles, policies, least privilege, trust relationships, resource-based policies
- Lambda — function creation, layers, environment variables, IAM execution roles, testing
- CDK — stacks, constructs, deploy, synth, diff, destroy, cross-stack references
- EventBridge — rules, targets, event patterns, scheduled triggers
- CloudWatch — log groups, log insights queries, metric alarms, dashboard creation
- AWS CLI — profiles, regions, common commands for every service above

### AWS Bedrock — Full Mastery
- Foundation Models — what they are, how to choose, pricing, token limits, latency trade-offs
- Model invocation API — request format, response parsing, streaming responses, error handling
- Knowledge Bases — creation, S3 data sources, embeddings models, chunking strategies, sync, query API, citations
- Agents — creation, instruction prompts, action groups, OpenAPI schemas, Lambda integration, KB association, trace reading
- Guardrails — PHI/PII masking, topic filters, word filters, content filters, attaching to agents
- Bedrock Studio — visual testing and prototyping tool
- Pricing — how to estimate and control costs for all Bedrock features

### AI and ML Concepts
- What foundation models are and how they differ from traditional ML models
- How LLMs are trained — pre-training, fine-tuning, RLHF
- Embeddings — how text becomes vectors, what cosine similarity means
- Vector search — approximate nearest neighbor, why it is faster than exact search
- RAG — Retrieval Augmented Generation, why it beats fine-tuning for most use cases
- Chunking strategies — fixed size, semantic, hierarchical, overlap
- Prompt engineering — system prompts, few-shot examples, chain of thought, structured output
- ReAct pattern — how agents reason, act, and observe in loops
- Token economics — what tokens are, how to count them, how to reduce costs
- Model evaluation — what metrics matter, how to test answer quality

### Healthcare Domain
- FHIR R4 — resource types, Bundle structure, Patient, Condition, MedicationRequest, Observation, Encounter
- Synthea — what it is, how to configure it, what it generates, how to use the output
- HIPAA — what PHI is, what ePHI is, what HIPAA-eligible means on AWS, what you must never do
- Clinical data modeling — how to flatten FHIR for analytics, what fields matter
- Drug interactions — what they are, severity levels, how clinical decision support works

### Data Engineering — Month 3
- AWS Glue — crawlers, Data Catalog, ETL jobs, PySpark basics, job bookmarks, triggers
- Apache Parquet — why it is better than JSON and CSV for analytics, how columnar storage works
- Amazon Athena — databases, tables, partitioning, cost optimization, query result locations
- Data pipeline design — source, transform, sink pattern, idempotency, error handling

---

## What You Will Build

### Project: ClinicalMind

A HIPAA-ready clinical AI agent that answers medical questions grounded in structured patient data and clinical documents. Built on AWS Bedrock. Deployed via AWS CDK. Costs $10/month to run.

**The problem it solves:**
Healthcare staff spend hours manually searching clinical guidelines and patient records. ClinicalMind answers complex clinical questions in seconds, grounded in real documents, citing exactly which source it used. No hallucinations — every answer is traceable.

**Full system architecture:**

```
Synthea Generator
      |
      | FHIR JSON files
      v
Amazon S3 (clinicalmind-patients bucket)
      |                    |
      | raw FHIR           | documents
      v                    v
AWS Glue ETL          Bedrock Knowledge Base
      |                    |
      | Parquet             | embeddings + vector index
      v                    |
Amazon Athena              |
      |                    |
      | SQL results         |
      v                    v
Lambda Tools ---------> Bedrock Agent <--- Guardrails (PHI filter)
  get_patient_summary        |
  check_drug_interactions    |
  run_clinical_query         v
                        Final Answer with Citations
```

**Example interaction:**

Doctor asks: "Summarize patient John Smith and flag any medication risks"

ClinicalMind:
- Calls get_patient_summary → fetches FHIR record from S3
- Calls check_drug_interactions → checks medications against interaction table
- Queries Knowledge Base → finds relevant treatment protocol
- Calls run_clinical_query → gets population stats from Athena
- Guardrail scans response → masks any PHI
- Returns: structured cited answer with flags and protocol references

---

## Prerequisites — Verify Before Starting

Run every verification command. Do not start Day 1 until all pass.

AWS account created at aws.amazon.com — free tier available
AWS CLI installed: run aws --version — should return version 2.x or higher
AWS CLI configured: run aws sts get-caller-identity — should return your account ID
Python 3.10 or higher: run python3 --version
Node.js 18 or higher: run node --version
AWS CDK: run npm install -g aws-cdk then cdk --version
Java 17 or higher (for Synthea): run java -version
Git configured: run git config --global user.name
boto3 installed: run pip3 install boto3
Bedrock enabled: go to AWS console → Bedrock → Model Access → enable Claude Haiku in us-east-1

---

## Repository Structure

When starting Month 1 Day 1, Claude Code scaffolds this exact structure. Every folder gets a README.md. Nothing is left undocumented.

```
clinicalmind/
│
├── CLINICALMIND_MASTER.md        this file — course and reference
├── README.md                     project overview for GitHub
├── ARCHITECTURE.md               architecture decisions and diagrams
├── .env.example                  all environment variables with descriptions
├── .gitignore                    node_modules, .env, dist, cdk.out, pycache
│
├── scripts/
│   ├── hello_bedrock.py          first Bedrock API call in Python
│   ├── hello_bedrock.ts          first Bedrock API call in TypeScript
│   ├── compare_apis.py           Anthropic vs Bedrock side by side
│   └── query_kb.py               Knowledge Base query with citations
│
├── data/
│   ├── generate/
│   │   ├── README.md             Synthea instructions
│   │   └── generate.sh           automates Synthea download and run
│   ├── sample/                   3 to 5 committed sample FHIR files
│   └── guidelines/
│       └── treatment_protocols.md  fake clinical guidelines document
│
├── infra/
│   ├── README.md                 deployment instructions
│   ├── package.json
│   ├── cdk.json
│   └── lib/
│       ├── clinicalmind-stack.ts  main stack — S3, Lambda, Guardrail
│       ├── knowledge-base-stack.ts  KB and data source
│       └── agent-stack.ts        Agent, action groups, KB association
│
├── agent/
│   ├── README.md                 agent architecture explanation
│   ├── agent-definition.json     agent config and instruction prompt
│   └── tools/
│       ├── get_patient_summary/
│       │   ├── handler.py
│       │   └── requirements.txt
│       ├── check_drug_interactions/
│       │   ├── handler.py
│       │   └── interactions.json
│       └── run_clinical_query/   added in Month 3
│           ├── handler.py
│           └── requirements.txt
│
├── knowledge-base/
│   ├── README.md
│   └── sync.sh                   upload to S3 and trigger KB sync
│
├── guardrails/
│   ├── README.md
│   └── guardrail-config.json
│
├── etl/                          added in Month 3
│   ├── README.md
│   ├── glue_job.py               PySpark transformation script
│   └── athena_queries/
│       └── patient_analytics.sql  5 clinical analytics queries
│
└── demo/
    ├── screenshots/
    ├── demo.gif
    ├── linkedin-post.md
    └── medium-article-outline.md
```

---

---

# MONTH 1 — BUILD

---

## WEEK 1: AWS Setup and Bedrock Basics

**Weekly goal:** Have a working AWS environment, understand how Bedrock differs from the Anthropic API, generate fake FHIR patient data, and upload it to S3.

**What you understand by end of this week:**
- Why companies use Bedrock instead of Anthropic directly
- How AWS authentication works and why it is more secure than API keys in code
- What FHIR data looks like and why Synthea is the right tool for fake data
- How to navigate the AWS console, CLI, and SDK confidently

---

### Day 1 — Project Scaffold and AWS Verification

**Session prompt:**
"I am on Month 1 Week 1 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Scaffold the complete project folder structure exactly as defined in the Repository Structure section. Create .gitignore, .env.example with all placeholder variables, and a minimal README.md. Initialize git, make the first commit. Then verify my AWS CLI is configured correctly by running aws sts get-caller-identity and confirm Bedrock is accessible in us-east-1."

**What gets built:**
- Complete folder structure created with placeholder README.md in every folder
- .gitignore covering node_modules, .env, dist, cdk.out, __pycache__, .DS_Store, *.jar
- .env.example with: AWS_REGION, AWS_ACCOUNT_ID, S3_BUCKET_NAME, KNOWLEDGE_BASE_ID, AGENT_ID, GUARDRAIL_ID
- README.md with project name and one-line description
- Git initialized, first commit made with message "chore: initial project scaffold"

**Concepts Claude Code teaches today:**
- Why .gitignore matters — never commit credentials or build artifacts
- What .env.example is for — shows teammates what variables are needed without exposing values
- How AWS CLI authentication works — credentials file, environment variables, IAM roles

**Definition of done:**
Running aws sts get-caller-identity returns your Account ID without errors. Project folder exists in GitHub with first commit visible.

---

### Day 2 — Explore the Bedrock Console

**Session prompt:**
"I am on Month 1 Week 1 Day 2 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Guide me through enabling Bedrock model access in the AWS console for Claude Haiku in us-east-1. Explain what each available foundation model is and when you would choose it over others. Then walk me through the Bedrock playground — help me send a healthcare question to Claude Haiku and read the token count and latency. Explain everything I am seeing."

**What you do:**
- AWS console → Bedrock → Model Access → request Claude Haiku access
- Explore the model catalog — read descriptions and pricing for Claude Haiku, Sonnet, Titan, Llama
- Open playground → select Claude Haiku → send: "What is FHIR R4 and why does it matter in healthcare?"
- Read the response, note the input tokens, output tokens, and response latency shown

**Concepts Claude Code teaches today:**
- Foundation model tiers — Haiku is cheapest and fastest, Sonnet is smarter and costlier
- Bedrock playground vs API — playground is for manual testing, API is for your application
- Token pricing — you pay for what you use, input and output tokens priced separately
- Why Claude Haiku is the right choice for this learning project — cost stays under $10/month

**Definition of done:**
Claude Haiku responds in the Bedrock playground. You can describe what input tokens and output tokens mean.

---

### Day 3 — First Bedrock API Call in Python

**Session prompt:**
"I am on Month 1 Week 1 Day 3 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create scripts/hello_bedrock.py that calls Claude Haiku via the Bedrock API. Ask it: what are the most important FHIR R4 resource types for an EHR system? Print the response. Set up a virtual environment and requirements.txt with boto3. Explain every part of the code as you write it — the client setup, the request body, the response parsing."

**What gets built:**
- venv created and activated
- requirements.txt with boto3
- scripts/hello_bedrock.py — full working Bedrock call

**Concepts Claude Code teaches today:**
- boto3 is the Python AWS SDK — one library to access every AWS service
- bedrock-runtime is the specific service client for calling foundation models
- The request body uses the same format as Anthropic's API but is wrapped in AWS conventions
- AWS credentials come from your CLI config — never hardcode them in scripts
- Error handling — what happens when model access is not enabled, what HTTP errors mean

**Definition of done:**
Running python3 scripts/hello_bedrock.py prints a coherent response about FHIR resources from Claude Haiku.

---

### Day 4 — First Bedrock API Call in TypeScript

**Session prompt:**
"I am on Month 1 Week 1 Day 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create scripts/hello_bedrock.ts that does the same as yesterday's Python script but in TypeScript. Use AWS SDK v3. Set up package.json with @aws-sdk/client-bedrock-runtime and ts-node. Explain the differences between the Python and TypeScript approaches — client instantiation, async handling, response parsing."

**What gets built:**
- package.json at root with @aws-sdk/client-bedrock-runtime and ts-node as dev dependency
- tsconfig.json configured for Node.js
- scripts/hello_bedrock.ts — full working TypeScript Bedrock call

**Concepts Claude Code teaches today:**
- AWS SDK v3 uses a client-command pattern instead of direct method calls
- TypeScript gives you type safety — InvokeModelCommand has typed input and output
- Async/await is required — Bedrock calls are always asynchronous
- The same IAM credentials work for Python boto3 and TypeScript SDK

**Definition of done:**
Running npx ts-node scripts/hello_bedrock.ts prints a response from Claude Haiku.

---

### Day 5 — Compare Anthropic API vs Bedrock API

**Session prompt:**
"I am on Month 1 Week 1 Day 5 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create scripts/compare_apis.py that sends the same prompt to Claude Haiku using both the Anthropic SDK and the Bedrock API. Print both responses, both latencies, and the token counts side by side. Then write a comparison section in ARCHITECTURE.md explaining when to use each and why ClinicalMind uses Bedrock."

**What gets built:**
- scripts/compare_apis.py — dual API call with timing
- ARCHITECTURE.md populated with first real content — Anthropic vs Bedrock decision

**Concepts Claude Code teaches today:**
- Anthropic API: simpler auth, direct billing, not inside your AWS account, not HIPAA eligible
- Bedrock: AWS IAM auth, AWS billing, stays inside your VPC, HIPAA eligible, enterprise-grade
- For personal projects use Anthropic — simpler setup, no AWS dependency
- For anything with real patient data or enterprise compliance, always use Bedrock
- Latency is usually slightly higher on Bedrock because of the AWS routing layer

**Definition of done:**
Script runs, prints both responses, both latencies. ARCHITECTURE.md has a clear written explanation.

---

### Day 6 — Generate Fake Patient Data with Synthea

**Session prompt:**
"I am on Month 1 Week 1 Day 6 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Help me download Synthea and generate 100 fake FHIR R4 patients with diabetes and hypertension conditions. Put output in data/sample/. Write data/generate/generate.sh that automates the download and generation so anyone can reproduce it. Write data/generate/README.md. Then open one patient file and explain the FHIR Bundle structure to me — what every resource type means."

**What gets built:**
- Synthea JAR downloaded
- 100 fake FHIR patients generated in data/sample/
- data/generate/generate.sh — one command to regenerate all data
- data/generate/README.md — Synthea explanation and usage instructions
- 3 sample files committed to repo, rest added to .gitignore

**Concepts Claude Code teaches today:**
- Synthea is built by MITRE Corporation specifically for testing healthcare software
- Each patient is a FHIR Bundle — a container resource holding all data about one person
- Patient resource — demographics, name, birthdate, gender, address
- Condition resource — diagnosis with ICD-10 code and onset date
- MedicationRequest resource — prescribed drug with dosage and prescriber
- Observation resource — lab results, vitals, with LOINC codes
- Encounter resource — hospital visits with dates and diagnosis references
- Zero HIPAA risk — all data is mathematically generated, not derived from real people

**Definition of done:**
data/sample/ contains 100 JSON files. You can open one and identify the Patient, Condition, and MedicationRequest resources by name.

---

### Day 7 — Upload FHIR Data to S3 and Write Guidelines

**Session prompt:**
"I am on Month 1 Week 1 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create an S3 bucket using the AWS CLI. Write knowledge-base/sync.sh that uploads all FHIR files from data/sample/ to s3://bucket/patients/ and the guidelines document to s3://bucket/guidelines/. Write data/guidelines/treatment_protocols.md with realistic content covering: diabetes management, hypertension treatment, drug interaction warnings for lisinopril and metformin, HbA1c monitoring schedule, and readmission risk factors. Commit everything. Tag this as end-of-week-1."

**What gets built:**
- S3 bucket created: clinicalmind-{account-id}
- knowledge-base/sync.sh — upload + sync in one command
- data/guidelines/treatment_protocols.md — minimum 500 words of realistic clinical content
- knowledge-base/README.md written
- All changes committed, git tag week-1-complete

**Definition of done:**
Running aws s3 ls s3://your-bucket/ shows patients/ and guidelines/ prefixes. treatment_protocols.md reads like a real clinical document.

---

## WEEK 2: Knowledge Bases

**Weekly goal:** Connect your S3 documents to a Bedrock Knowledge Base. Query it via API and get answers with citations. Understand why RAG is better than giving everything to the model at once.

**What you understand by end of this week:**
- What embeddings are in plain terms — not just the definition but the intuition
- Why RAG produces more accurate and trustworthy answers than raw model calls
- How to evaluate answer quality — when chunking strategy actually matters
- How to cite sources programmatically from KB responses

---

### Day 1 — Understand Embeddings and RAG

**Session prompt:**
"I am on Month 1 Week 2 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. No code today. Teach me embeddings, vector search, and RAG from scratch using simple analogies. Then explain exactly what happens inside a Bedrock Knowledge Base when I upload a document and when I query it. What is happening at each step? What is the vector database? What is cosine similarity? Why does chunking matter? Connect everything back to ClinicalMind."

**What you learn today — no code:**
- Embeddings: text converted to a list of numbers that captures meaning. Similar meaning = numbers that are close together in space.
- Vector search: instead of matching exact words, find documents whose number-vectors are closest to your question's number-vector. Finds relevant content even when words do not match.
- Chunking: documents split into small pieces before embedding. Chunk size affects retrieval quality.
- RAG loop: embed question → search vector DB → retrieve relevant chunks → send chunks + question to model → model answers using only retrieved content.
- Why RAG beats fine-tuning: fine-tuning changes the model permanently and costs thousands. RAG just retrieves relevant context at query time — cheaper, updatable, traceable.
- What Bedrock Knowledge Base does: automates all of this — you upload files, it chunks, embeds, indexes, and retrieves.

**Definition of done:**
You can explain RAG to someone in 3 sentences without looking at notes.

---

### Day 2 — Create Bedrock Knowledge Base

**Session prompt:**
"I am on Month 1 Week 2 Day 2 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Guide me through creating a Bedrock Knowledge Base in the AWS console step by step. Name it ClinicalMind-KB. Point it at my S3 bucket. Use Amazon Titan Embeddings V2 as the embedding model. Use the default managed vector store. Then write the CDK code for this KB in infra/lib/knowledge-base-stack.ts."

**What gets built:**
- Bedrock Knowledge Base created in console — status Ready
- infra/lib/knowledge-base-stack.ts — CDK definition
- KNOWLEDGE_BASE_ID added to .env.example

**Concepts Claude Code teaches today:**
- Embedding model converts your documents to vectors — Titan V2 is the best AWS-native option
- Managed vector store means AWS handles the vector database for you — no OpenSearch to manage
- Data source = the S3 connection — you can have multiple data sources per KB
- Sync status — you must trigger a sync after any S3 changes

**Definition of done:**
Knowledge Base shows status Active in console. Data source shows your S3 bucket.

---

### Day 3 — Sync and Verify Knowledge Base

**Session prompt:**
"I am on Month 1 Week 2 Day 3 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Trigger a sync of the ClinicalMind-KB Knowledge Base so it reads all FHIR files and the guidelines document from S3. Monitor the sync progress. After it completes, check the document count. Update knowledge-base/sync.sh to include the sync trigger command so uploading and syncing happen in one step. Test the sync end to end."

**What gets built:**
- Knowledge Base synced — all documents indexed
- knowledge-base/sync.sh updated with sync trigger
- Sync completion verified in console

**Concepts Claude Code teaches today:**
- Sync reads every file in S3, chunks it, embeds each chunk, stores in vector index
- Large files take longer — a 100-page PDF takes minutes, a small JSON is seconds
- Document count in console should match your S3 file count
- Re-syncing is safe — it is idempotent, updates changed files only

**Definition of done:**
Sync shows Completed status. Document count is non-zero.

---

### Day 4 — Query Knowledge Base via API with Citations

**Session prompt:**
"I am on Month 1 Week 2 Day 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create scripts/query_kb.py that queries ClinicalMind-KB using the retrieve_and_generate API. Test it with three questions: what medications is a diabetic patient typically on, what is the HbA1c monitoring schedule, and what are the drug interactions for lisinopril. For each response print the answer and the full citation list showing which S3 file and chunk was used."

**What gets built:**
- scripts/query_kb.py — full KB query script with citation printing

**Concepts Claude Code teaches today:**
- retrieve_and_generate does two things in one call: retrieves relevant chunks then generates an answer
- Citations are the key differentiator from a raw model call — every claim is traceable
- The citation shows S3 URI, chunk text, and relevance score
- If the KB returns wrong answers, the problem is usually chunking strategy or missing content

**Definition of done:**
All three test questions return coherent answers. Each answer has at least one citation pointing to an S3 file.

---

### Day 5 — Experiment with Chunking Strategies

**Session prompt:**
"I am on Month 1 Week 2 Day 5 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Change the ClinicalMind-KB chunking strategy from default fixed-size to semantic chunking. Re-sync the Knowledge Base. Run the same three test questions from yesterday. Compare the answers and citations — is the answer quality better or worse? Explain to me why chunking strategy affected the results."

**What gets built:**
- Knowledge Base updated to semantic chunking
- Re-sync completed
- Comparison notes written in ARCHITECTURE.md

**Concepts Claude Code teaches today:**
- Fixed-size chunking cuts at character count — fast but may split a sentence mid-thought
- Semantic chunking cuts at natural boundaries — paragraph ends, section breaks
- Better chunks = more relevant retrieval = better answers
- Clinical documents with structured sections benefit significantly from semantic chunking

**Definition of done:**
You can articulate why one chunking strategy produced better results than the other for your specific documents.

---

### Day 6 — Expand Clinical Guidelines Document

**Session prompt:**
"I am on Month 1 Week 2 Day 6 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Significantly expand data/guidelines/treatment_protocols.md. Add detailed sections on: hypertension medication ladder with specific drug names and doses, complete drug interaction table for the top 10 most common medications in your patient data, HbA1c target ranges by patient age and comorbidity, readmission risk scoring criteria, and medication reconciliation protocol. Re-sync the KB and verify the new content is retrievable with specific questions."

**What gets built:**
- treatment_protocols.md expanded to at least 1000 words of clinical content
- Knowledge Base re-synced
- 5 new specific questions answered correctly with citations from the new content

**Definition of done:**
Asking "What is the HbA1c target for a diabetic patient over 75?" returns a specific answer citing your treatment_protocols.md document.

---

### Day 7 — Document Week 2 and Commit

**Session prompt:**
"I am on Month 1 Week 2 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Write complete documentation for everything built this week. Update knowledge-base/README.md with full setup and query instructions. Update main README.md with a Knowledge Base section and an updated architecture description. Update ARCHITECTURE.md with your decision on which chunking strategy you chose and why. Commit all changes. Tag as week-2-complete."

**Definition of done:**
README.md clearly explains the Knowledge Base. knowledge-base/README.md has complete setup instructions. Git tag week-2-complete exists.

---

## WEEK 3: Bedrock Agents

**Weekly goal:** Build a Bedrock Agent with two Lambda tools. Watch it reason step by step, decide which tool to call, execute it, observe the result, and synthesize a final answer using both tool output and Knowledge Base content.

**What you understand by end of this week:**
- Why agents are fundamentally different from simple model calls
- How to design tools that an agent can use reliably
- How to read an agent trace and understand what the model was thinking
- Why OpenAPI schemas are required and how to write them correctly

---

### Day 1 — Understand the Agent Reasoning Pattern

**Session prompt:**
"I am on Month 1 Week 3 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. No code today. Teach me how Bedrock Agents work from first principles. What is the ReAct reasoning pattern? How does the agent decide which tool to call and when? What is an action group? What is an OpenAPI schema and why does the agent need it? What is the difference between calling a tool and querying the Knowledge Base? Walk me through exactly what happens step by step when I ask the agent to summarize a patient and check their medications."

**What you learn today:**
- ReAct = Reason, Act, Observe. The model generates a thought, selects a tool, calls it, reads the result, repeats until it has enough information to answer.
- Tools are Lambda functions. The agent does not execute code directly — it sends parameters to a Lambda and receives structured output.
- Action group = a named collection of tools with an OpenAPI schema describing each one.
- OpenAPI schema = a contract. It tells the agent the tool name, what it does, what parameters it needs, and what it returns. Without this the agent cannot call tools correctly.
- Knowledge Base retrieval is separate from tool calls — tools fetch specific data, KB retrieval finds relevant document passages.

**Definition of done:**
You can draw on paper the exact sequence of events when the agent answers "Does patient abc123 have any dangerous medication interactions?"

---

### Day 2 — Create the Bedrock Agent

**Session prompt:**
"I am on Month 1 Week 3 Day 2 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create a Bedrock Agent named ClinicalMind-Agent in the AWS console using Claude Haiku. Write a thorough agent instruction prompt that defines its role, behavior, tone, and what it must never do. Save the instruction to agent/agent-definition.json. Write the CDK code for the agent in infra/lib/agent-stack.ts. Test the agent in the console with a simple greeting to confirm it is active."

**What gets built:**
- Bedrock Agent created in console — status Active
- agent/agent-definition.json with full instruction prompt
- infra/lib/agent-stack.ts skeleton
- AGENT_ID added to .env.example

**Agent instruction prompt must include:**
- Role: clinical assistant for healthcare staff
- Capabilities: patient summaries, medication checks, protocol lookups
- Tone: professional, precise, never casual
- Constraints: never fabricate medical information, always cite sources, never give dosing advice not in the guidelines, refuse non-clinical questions politely

**Definition of done:**
Agent responds in the console test window. Asking "Hello, what can you help me with?" returns a response describing its clinical capabilities.

---

### Day 3 — Build Tool 1: get_patient_summary

**Session prompt:**
"I am on Month 1 Week 3 Day 3 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Build the get_patient_summary Lambda function in agent/tools/get_patient_summary/handler.py. It accepts a patient_id parameter. It fetches the FHIR JSON from S3 at patients/{patient_id}.json. It parses the Bundle, extracts: patient name, calculated age, gender, all active conditions with onset dates, all active medications with doses, most recent vitals, and most recent encounter date. It returns a clean structured dictionary. Write requirements.txt. Deploy to AWS Lambda. Test with a real patient ID from your Synthea data."

**What gets built:**
- agent/tools/get_patient_summary/handler.py — complete Lambda
- agent/tools/get_patient_summary/requirements.txt
- Lambda deployed with correct IAM role allowing S3 read access to your bucket
- Tested directly in Lambda console — response is a clean patient summary

**Concepts Claude Code teaches today:**
- Lambda execution role must have s3:GetObject permission on your bucket — principle of least privilege
- FHIR Bundle parsing — iterating entries, filtering by resourceType
- Age calculation from FHIR birthDate format
- Structuring Lambda return values so the agent can read them reliably

**Definition of done:**
Invoking the Lambda with a test event containing a valid patient_id returns a dictionary with name, age, conditions, medications, and vitals.

---

### Day 4 — Build Tool 2: check_drug_interactions

**Session prompt:**
"I am on Month 1 Week 3 Day 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Build the check_drug_interactions Lambda in agent/tools/check_drug_interactions/handler.py. It accepts a comma-separated list of medication names. It loads interactions.json which contains at least 20 drug interaction pairs. For every pair of medications in the input it checks the table and returns any matches with severity (HIGH, MODERATE, LOW) and a clinical note explaining the risk. If no interactions found return a clean safe result. Deploy and test."

**What gets built:**
- agent/tools/check_drug_interactions/interactions.json — 20+ drug interaction pairs covering common medications seen in diabetic and hypertensive patients
- agent/tools/check_drug_interactions/handler.py — complete Lambda with pairwise checking logic
- Lambda deployed and tested with real medication lists from your Synthea patients

**Interactions.json must cover:**
- lisinopril + NSAIDs — kidney function risk
- metformin + alcohol — lactic acidosis risk
- aspirin + warfarin — bleeding risk
- lisinopril + potassium supplements — hyperkalemia risk
- metformin + contrast dye — kidney failure risk
- amlodipine + simvastatin — myopathy risk
- At least 14 more clinically relevant pairs

**Definition of done:**
Lambda invoked with "lisinopril, aspirin, metformin, potassium" returns at least two flagged interactions with severity and clinical notes.

---

### Day 5 — Connect Tools to Agent via Action Groups

**Session prompt:**
"I am on Month 1 Week 3 Day 5 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create two action groups on the ClinicalMind-Agent. PatientActions wrapping get_patient_summary. ClinicalActions wrapping check_drug_interactions. Write the OpenAPI schema for each tool. Grant the agent permission to invoke both Lambdas. Test the agent in the console by asking it to summarize a specific patient by ID and verify it calls the Lambda and uses real data in its response."

**What gets built:**
- Action group PatientActions with OpenAPI schema for get_patient_summary
- Action group ClinicalActions with OpenAPI schema for check_drug_interactions
- IAM resource-based policies on both Lambdas allowing bedrock.amazonaws.com to invoke them
- Agent tested — confirms real Lambda call and data in response

**Concepts Claude Code teaches today:**
- OpenAPI schema must accurately describe the tool or the agent will call it incorrectly
- The description field is critical — the agent reads it to decide when to use each tool
- Lambda resource-based policies are different from IAM role policies — both are required
- Action group status must be Enabled before the agent can use it

**Definition of done:**
Asking the agent "Summarize patient [real patient ID from your data]" returns a response containing real data from your S3 FHIR file — not a fabricated answer.

---

### Day 6 — Connect Agent to Knowledge Base

**Session prompt:**
"I am on Month 1 Week 3 Day 6 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Associate ClinicalMind-KB with ClinicalMind-Agent. Then test the full combined flow with a question that requires both tools and KB: ask the agent to summarize a patient, check their medications for interactions, and tell you what the treatment protocol says about their primary diagnosis. Verify the response uses data from the Lambda tool calls AND cites the treatment_protocols.md document."

**What gets built:**
- KB associated with agent in console
- infra/lib/agent-stack.ts updated with KB association
- Full end-to-end test documented in demo/screenshots/

**Definition of done:**
Single question triggers: at least one Lambda tool call, at least one KB retrieval. Final response includes real patient data and a citation to your guidelines document.

---

### Day 7 — Read Agent Traces and Document

**Session prompt:**
"I am on Month 1 Week 3 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Enable trace logging on the agent. Run the full end-to-end test again. Read every step of the trace output and explain what the model decided at each point — when it reasoned, when it chose to call a tool, what it sent, what it received, and how it synthesized the final answer. Write agent/README.md explaining the architecture, tools, KB connection, and reasoning pattern. Commit everything. Tag week-3-complete."

**What gets built:**
- Traces enabled and read in console
- agent/README.md — complete architecture explanation with tool descriptions
- All changes committed, git tag week-3-complete

**Definition of done:**
You can read a raw trace and narrate what the agent was doing at every step without assistance.

---

## WEEK 4: Guardrails and CDK Deployment

**Weekly goal:** Add safety controls that filter PHI and off-topic content. Deploy the entire system with one CDK command. Produce a polished GitHub repository ready to show anyone.

**What you understand by end of this week:**
- How Guardrails intercept responses and why this is different from prompt engineering
- How CDK orchestrates the deployment of interconnected AWS resources
- What makes a GitHub repository professional vs just a code dump
- How to present a project so the value is immediately obvious

---

### Day 1 — Create Guardrail with PHI Masking

**Session prompt:**
"I am on Month 1 Week 4 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create a Bedrock Guardrail named ClinicalMind-Guard. Enable sensitive information filters for: names, dates of birth, phone numbers, email addresses, social security numbers, and medical record numbers. Set the action to MASK. Save the full guardrail configuration to guardrails/guardrail-config.json. Write CDK for this guardrail. Test it by passing a response containing fake PHI through the guardrail API and confirm the identifiers are masked."

**What gets built:**
- Bedrock Guardrail created — PHI masking enabled for 6 identifier types
- guardrails/guardrail-config.json — complete configuration
- guardrails/README.md explaining what the guardrail does and why
- GUARDRAIL_ID added to .env.example
- Test confirms masking works

**Concepts Claude Code teaches today:**
- Guardrails are a separate AWS resource — not part of the model, not part of the agent
- They apply as an independent layer — responses pass through guardrail before reaching the caller
- MASK replaces PHI with a placeholder like [NAME] or [DATE_OF_BIRTH]
- BLOCK would refuse the entire response — too aggressive for this use case
- This is one of the controls AWS uses to claim HIPAA eligibility for Bedrock

**Definition of done:**
A test response containing "Patient John Smith born 1964-03-15, SSN 123-45-6789" returns with those values masked.

---

### Day 2 — Add Topic Filter and Content Filter

**Session prompt:**
"I am on Month 1 Week 4 Day 2 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Add two more controls to ClinicalMind-Guard. First: a denied topic filter that blocks questions and responses unrelated to clinical care, patient management, and medical protocols. Second: a content filter set to block harmful content at medium strength. Update guardrail-config.json. Test the topic filter by asking the agent a completely off-topic question and verify it refuses politely. Test that clinical questions still work normally."

**What gets built:**
- Denied topic added to guardrail: non-medical topics with examples
- Content filter enabled at medium strength
- guardrail-config.json updated
- Two tests: off-topic refuses, clinical question answers

**Definition of done:**
"What is a good pasta recipe?" returns a polite refusal. "What are the symptoms of hyperkalemia?" returns a clinical answer.

---

### Day 3 — Write the Complete CDK Stack

**Session prompt:**
"I am on Month 1 Week 4 Day 3 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Write the complete CDK stack that deploys the entire ClinicalMind system in one command. Include: S3 bucket with encryption and block public access, both Lambda functions with correct execution roles and least-privilege S3 permissions, the Knowledge Base with S3 data source, the Bedrock Agent with both action groups and KB association, and the Guardrail attached to the agent. Run cdk synth and fix all errors until it produces a valid CloudFormation template."

**What gets built:**
- infra/lib/clinicalmind-stack.ts — complete unified stack
- All IAM roles with least-privilege policies
- Cross-stack references wired correctly
- cdk synth passes with no errors

**Concepts Claude Code teaches today:**
- CDK constructs represent AWS resources as TypeScript classes
- IAM roles must be created for each Lambda with only the permissions it needs
- Order of resource creation matters — S3 bucket must exist before KB references it
- CDK outputs can print important resource IDs after deployment

**Definition of done:**
cdk synth produces a CloudFormation template. cdk diff shows all expected resources.

---

### Day 4 — Deploy and Test End to End

**Session prompt:**
"I am on Month 1 Week 4 Day 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Run cdk deploy. Fix any errors that appear. After successful deployment, run the complete end-to-end test: sync FHIR data to S3, sync KB, then ask the agent a complex clinical question. Verify the CDK-deployed version works identically to the manually configured version. Document any differences."

**What gets built:**
- Full stack deployed to AWS via CDK
- CDK outputs captured and added to README
- End-to-end test confirmed on deployed infrastructure

**Definition of done:**
cdk deploy completes with no errors. Agent responds correctly. All resource IDs from CDK outputs match what is in .env.example.

---

### Day 5 — Write Professional README and Architecture Docs

**Session prompt:**
"I am on Month 1 Week 4 Day 5 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Write a complete professional README.md. It must include: a compelling one-paragraph description, an ASCII art architecture diagram showing the full data flow, a tech stack table, a cost estimate table, prerequisites list, step-by-step setup instructions that a new engineer could follow from zero, usage examples with real sample questions and their expected outputs, and a section explaining how each HIPAA-eligibility control works. Also complete ARCHITECTURE.md with all design decisions."

**What gets built:**
- README.md — complete, professional, ready for GitHub
- ARCHITECTURE.md — all design decisions documented with rationale

**Definition of done:**
Show README to Claude Code and ask: "Could a new engineer set up this project following only this README?" If yes, done.

---

### Day 6 — Record Demo and Prepare Assets

**Session prompt:**
"I am on Month 1 Week 4 Day 6 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Help me capture demo assets. Run three showcase test questions that demonstrate all capabilities: one using get_patient_summary, one using check_drug_interactions, one requiring KB retrieval and citations. Take clear screenshots of each response including the full answer and citations. Write captions for each screenshot. Draft the LinkedIn post in demo/linkedin-post.md. Write the Medium article outline in demo/medium-article-outline.md."

**What gets built:**
- demo/screenshots/ with at least 3 clear annotated screenshots
- demo/linkedin-post.md — ready to publish
- demo/medium-article-outline.md — section by section outline

**LinkedIn post must:**
- Be under 200 words
- Mention FHIR, Bedrock, HIPAA
- Include the cost figure — $10/month
- End with a question to drive comments
- Not use the word "excited" or "thrilled"

**Definition of done:**
Screenshots are clear enough that someone who has never seen the project understands what it does.

---

### Day 7 — Final Review, Tag, and Publish

**Session prompt:**
"I am on Month 1 Week 4 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Do a complete repository audit. Check every folder has a README. Verify .env is not committed. Verify .gitignore covers all the right patterns. Check that no AWS account IDs or credentials are hardcoded anywhere. Verify all READMEs are accurate and complete. Make a final commit. Create git tag v1.0.0 and push it. Then publish the LinkedIn post from demo/linkedin-post.md."

**Definition of done:**
Repository is clean. Tag v1.0.0 exists on GitHub. LinkedIn post is published. GitHub repo URL is in your LinkedIn Featured section.

---

---

# MONTH 2 — CERTIFY

## AWS Certified AI Practitioner (AIF-C01)

This month has no coding. It is dedicated entirely to earning your first AWS certification.
Do not rush. Do not cram Week 4. Study every day for 30 to 60 minutes.

---

### About the Exam

| Detail | Value |
|--------|-------|
| Exam code | AIF-C01 |
| Cost | $150 USD |
| Questions | 85 questions |
| Duration | 90 minutes |
| Passing score | 700 out of 1000 |
| Format | Multiple choice and multiple response |
| Delivery | Online proctored from home via Pearson VUE |
| Valid for | 3 years from passing date |

Book at aws.amazon.com/certification. You can take it online from home with no test center.

---

### Exam Domain Breakdown

| Domain | Weight | Topics |
|--------|--------|--------|
| Fundamentals of AI and ML | 20% | ML types, training, evaluation, model lifecycle |
| Fundamentals of Generative AI | 24% | Foundation models, LLMs, prompt engineering, fine-tuning vs RAG |
| Applications of Foundation Models | 28% | Bedrock, SageMaker, Amazon AI services, use case selection |
| Guidelines for Responsible AI | 14% | Bias, fairness, explainability, transparency, HIPAA, regulation |
| Security, Compliance, and Governance | 14% | IAM, data governance, Guardrails, compliance frameworks |

---

### Week 1 — AI and ML Fundamentals

**Session prompt:**
"I am on Month 2 Week 1 of the ClinicalMind course studying for the AWS AI Practitioner exam. Read CLINICALMIND_MASTER.md. Teach me everything in the AI and ML Fundamentals domain. Cover: supervised learning, unsupervised learning, reinforcement learning, what a neural network is, what training data and labels are, what a model is, what inference means, what overfitting is, how models are evaluated, precision vs recall, and what the ML lifecycle looks like. Use plain language and healthcare examples wherever possible. After teaching, quiz me with 10 questions."

**Topics to master this week:**
- Supervised learning — input-output pairs, classification, regression
- Unsupervised learning — clustering, anomaly detection, no labels needed
- Reinforcement learning — agent, environment, reward, policy
- Neural networks — layers, activation functions, forward pass
- Training — gradient descent, loss function, epochs, batches
- Overfitting vs underfitting — bias-variance trade-off
- Evaluation metrics — accuracy, precision, recall, F1, AUC-ROC
- ML pipeline — data collection, feature engineering, training, evaluation, deployment, monitoring

---

### Week 2 — Generative AI and Foundation Models

**Session prompt:**
"I am on Month 2 Week 2 of the ClinicalMind course studying for the AWS AI Practitioner exam. Read CLINICALMIND_MASTER.md. Teach me everything in the Generative AI and Foundation Models domain. Cover: what makes a model a foundation model, how LLMs are trained, what RLHF is, what prompt engineering is and its main techniques, what fine-tuning is and when to use it vs RAG, what temperature and top-p are, what hallucination is and why it happens, and what multimodal models are. Use examples from the ClinicalMind project where possible. Quiz me with 15 questions after."

**Topics to master this week:**
- Foundation models — pre-trained on massive data, general purpose, adaptable
- LLM training — pre-training on internet text, next-token prediction
- RLHF — Reinforcement Learning from Human Feedback, how Claude was trained
- Prompt engineering techniques — zero-shot, few-shot, chain of thought, system prompts
- Fine-tuning — when it makes sense, cost, when RAG is better
- Inference parameters — temperature controls randomness, top-p controls token selection
- Hallucination — model generates plausible but false content, why RAG reduces it
- Multimodal — models that handle text, images, audio together

---

### Week 3 — AWS AI Services and Responsible AI

**Session prompt:**
"I am on Month 2 Week 3 of the ClinicalMind course studying for the AWS AI Practitioner exam. Read CLINICALMIND_MASTER.md. Teach me two things today. First: every AWS AI service on the exam — what it does, what problem it solves, when to choose it. Cover Bedrock, SageMaker, Rekognition, Comprehend, Textract, Transcribe, Polly, Translate, Forecast, Personalize, and Lex. Second: Responsible AI — bias types, fairness definitions, explainability, transparency, what HIPAA means for AI, what AWS does to support compliance. Quiz me with 20 questions mixing both topics."

**AWS AI services to know:**
- Bedrock — foundation model API, Knowledge Bases, Agents, Guardrails
- SageMaker — full ML platform, build-train-deploy custom models
- Rekognition — image and video analysis, face detection, content moderation
- Comprehend — NLP, sentiment analysis, entity recognition, medical version for clinical text
- Textract — extract text and structured data from documents and forms
- Transcribe — speech to text, medical version for clinical dictation
- Polly — text to speech
- Translate — language translation
- Forecast — time-series forecasting
- Personalize — recommendation systems
- Lex — chatbot building, conversational AI

**Responsible AI topics:**
- Bias sources — data bias, measurement bias, aggregation bias
- Fairness — demographic parity, equal opportunity
- Explainability — LIME, SHAP, what black-box means
- Transparency — model cards, data sheets
- HIPAA — what makes a service HIPAA-eligible, BAA requirement
- AWS Guardrails — how they support responsible deployment

---

### Week 4 — Practice Exams and Exam Day

**Session prompt:**
"I am on Month 2 Week 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. I am doing final exam preparation for the AWS AI Practitioner AIF-C01. Give me a full 50-question practice exam covering all five domains proportionally weighted. Present one question at a time. After I answer, tell me if I am correct, explain why, and reference the relevant service or concept. Track my score. At the end give me a domain breakdown of my results and tell me which areas need more review before I sit the real exam."

**Exam week checklist:**
- Score 85%+ on practice questions before booking
- Book at aws.amazon.com/certification via Pearson VUE online
- Test your computer — webcam, microphone, stable internet, clean desk
- No notes, no second monitor, no phone on desk during exam
- Have government photo ID ready
- Log in 15 minutes before exam start time

**After passing:**
- Download badge from Credly
- Add certification to LinkedIn — Certifications section
- Share the Credly badge as a LinkedIn post
- Add to GitHub profile README

---

---

# MONTH 3 — EXPAND

---

## WEEK 1: AWS Glue — Catalog FHIR Data

**Weekly goal:** Set up a Glue Crawler that automatically discovers and catalogs the schema of your FHIR JSON files. Understand how the Glue Data Catalog works and what it enables.

**What you understand by end of this week:**
- Why schema discovery matters for large datasets
- What the Glue Data Catalog is and how Athena uses it
- Why schema-on-read is powerful for clinical data

---

### Day 1 — Understand Glue Architecture

**Session prompt:**
"I am on Month 3 Week 1 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. No code today. Teach me how AWS Glue works from first principles. What is a crawler? What is the Glue Data Catalog? What is a database and table in Glue? How does Glue relate to Athena? What is the difference between schema-on-write and schema-on-read? How does Parquet differ from JSON for analytics? Why would I convert my FHIR JSON to Parquet?"

**Definition of done:**
You can explain why JSON in S3 + Glue + Athena is a valid analytics stack and why Parquet is faster and cheaper for queries.

---

### Day 2 — Create and Run a Glue Crawler

**Session prompt:**
"I am on Month 3 Week 1 Day 2 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create an AWS Glue Crawler named clinicalmind-fhir-crawler that points at the s3://bucket/patients/ prefix. Set the target database to clinicalmind_raw. Run the crawler. Examine the tables it discovered. Write the CDK code for this crawler in infra/lib/clinicalmind-stack.ts. Document what schema the crawler inferred from the FHIR JSON files."

**What gets built:**
- Glue Crawler created and run
- clinicalmind_raw database populated with discovered tables
- CDK definition for crawler
- etl/README.md started with architecture explanation

**Definition of done:**
Glue Data Catalog shows a database with at least one table containing inferred columns from your FHIR JSON.

---

### Days 3 to 5 — Explore Catalog and Plan ETL

**Session prompt:**
"I am on Month 3 Week 1 Day 3 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Open the Glue Data Catalog and explore the discovered schema. Show me how to browse tables and preview data. Explain what the crawler got right and what it got wrong — FHIR nested JSON is complex and crawlers often struggle with deeply nested arrays. Plan the ETL transformation we will write next week: what fields do we want in the final flat table, what should the Parquet schema look like, what are the target columns and their types."

**Definition of done:**
etl/README.md contains a planned output schema table showing target column names, types, and source FHIR path for each.

---

### Days 6 to 7 — CDK Infrastructure for ETL Layer and Document

**Session prompt:**
"I am on Month 3 Week 1 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Write the CDK infrastructure for the full ETL layer: the Glue database, the Glue IAM role with S3 and Glue permissions, the output S3 prefix for processed data, and an Athena workgroup with query result location. Commit all Week 1 Month 3 work. Tag as month-3-week-1-complete."

---

## WEEK 2: AWS Glue ETL Job

**Weekly goal:** Write a PySpark ETL job that transforms nested FHIR JSON into a clean flat Parquet table. Run it. Verify the output is queryable.

---

### Days 1 to 3 — Write the PySpark ETL Job

**Session prompt:**
"I am on Month 3 Week 2 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Write the Glue ETL job in etl/glue_job.py using PySpark. It should: read all FHIR JSON files from s3://bucket/patients/, parse the Bundle entries, extract one row per patient with columns: patient_id, full_name, birth_date, age_years, gender, primary_condition, all_conditions as array, all_medications as array, last_encounter_date, last_bp_systolic, last_bp_diastolic, last_glucose. Write the output as Parquet to s3://bucket/processed/patients/. Partition by primary_condition. Explain every PySpark operation as you write it."

**What gets built:**
- etl/glue_job.py — complete PySpark script
- Output Parquet files in S3 processed prefix
- Job run visible in Glue console

**Concepts Claude Code teaches today:**
- GlueContext vs SparkContext — what Glue adds to standard Spark
- DynamicFrame vs DataFrame — when to use each
- Exploding nested arrays in PySpark — how to flatten FHIR entry arrays
- Partitioning — writing Parquet with partition columns for faster Athena queries
- Job bookmarks — how Glue tracks which files it has already processed

---

### Days 4 to 5 — Deploy and Run the Job

**Session prompt:**
"I am on Month 3 Week 2 Day 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Deploy etl/glue_job.py to AWS Glue. Configure the job with appropriate worker type and count for this data size. Run the job. Monitor the run logs in CloudWatch. After completion, verify the Parquet output exists in S3 and has the expected schema. Fix any errors in the script."

**Definition of done:**
Glue job run completes with status Succeeded. S3 processed prefix contains Parquet files. aws s3 ls on the processed prefix shows files.

---

### Days 6 to 7 — Catalog Processed Data and Document

**Session prompt:**
"I am on Month 3 Week 2 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Create a second Glue Crawler that points at the processed Parquet output. Run it to catalog the clean schema. Verify the table in Glue Data Catalog has the expected column names and types. Update etl/README.md with the full ETL architecture, the job parameters, and the output schema. Commit and tag month-3-week-2-complete."

---

## WEEK 3: Amazon Athena

**Weekly goal:** Query your clean Parquet data with SQL. Write 5 clinical analytics queries. Understand partitioning, cost optimization, and how to connect Athena to external tools.

---

### Day 1 — Set Up Athena and Run First Query

**Session prompt:**
"I am on Month 3 Week 3 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Set up the Athena query editor pointing at the clinicalmind_processed database. Configure the query result location in S3. Run your first query: count all patients by primary condition, ordered by count descending. Explain how Athena pricing works — cost per TB scanned — and how Parquet partitioning reduces cost compared to scanning raw JSON."

**What gets built:**
- Athena workgroup configured
- First query run and results verified
- Cost comparison documented in ARCHITECTURE.md

---

### Days 2 to 4 — Write 5 Clinical Analytics Queries

**Session prompt:**
"I am on Month 3 Week 3 Day 2 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Write all 5 clinical analytics queries in etl/athena_queries/patient_analytics.sql. Each query should answer a clinically meaningful question: patient count and percentage by primary condition, average age by condition with standard deviation, top 10 most prescribed medications across all patients, patients with 3 or more comorbidities, and patients whose last encounter was more than 6 months ago flagged as potentially overdue. Run all 5. Verify results make clinical sense given 100 synthetic patients."

**What gets built:**
- etl/athena_queries/patient_analytics.sql with 5 complete queries
- All 5 run successfully with non-empty results

---

### Days 5 to 7 — Optimize and Document

**Session prompt:**
"I am on Month 3 Week 3 Day 7 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Review all 5 Athena queries for cost optimization — are they using partition pruning, are they selecting only needed columns, are they avoiding SELECT star. Update any inefficient queries. Add query cost estimates as comments in patient_analytics.sql. Update etl/README.md with the complete data pipeline documentation from raw FHIR to Parquet to Athena results. Commit and tag month-3-week-3-complete."

---

## WEEK 4: Athena Tool, Agent Update, and Certification Prep

**Weekly goal:** Add a third Lambda tool that lets the agent run Athena queries on demand. Update the agent. Begin AWS Data Engineer Associate exam preparation.

---

### Days 1 to 3 — Build and Connect run_clinical_query Tool

**Session prompt:**
"I am on Month 3 Week 4 Day 1 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Build agent/tools/run_clinical_query/handler.py. It accepts a clinical question in natural language. It converts the question to an Athena SQL query using a Claude Haiku call. It executes the query against the clinicalmind_processed database. It waits for completion. It returns the results as a structured table. Deploy the Lambda. Add it as a third action group AnalyticsActions on ClinicalMind-Agent. Test by asking the agent how many diabetic patients are in the system."

**What gets built:**
- agent/tools/run_clinical_query/handler.py — full Lambda with NL-to-SQL and Athena execution
- AnalyticsActions action group on agent
- Agent tested with analytics question

**Definition of done:**
Asking the agent "How many patients have diabetes?" triggers the Athena tool and returns an accurate count from your processed data.

---

### Days 4 to 5 — Final Repository Polish

**Session prompt:**
"I am on Month 3 Week 4 Day 4 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. Do a complete final review of the entire repository. Every README must be accurate and complete. ARCHITECTURE.md must reflect all Month 3 additions. The main README.md must be updated with the ETL pipeline and Athena tool. Run cdk synth to confirm all infrastructure is still valid. Make a final commit. Create git tag v2.0.0 for the Month 3 complete version."

---

### Days 6 to 7 — Begin Data Engineer Exam Prep

**Session prompt:**
"I am on Month 3 Week 4 Day 6 of the ClinicalMind course. Read CLINICALMIND_MASTER.md. I am starting preparation for the AWS Certified Data Engineer Associate exam DEA-C01. Teach me the exam domain breakdown, what each domain covers, and how my ClinicalMind project maps to exam content. Then quiz me on the topics I already know from building ClinicalMind: Glue, Athena, S3, Lambda, IAM, CDK. Identify the gaps — what I built versus what the exam covers that I have not touched yet."

---

---

# AWS CERTIFIED DATA ENGINEER ASSOCIATE — DEA-C01

Complete this certification after finishing Month 3. Estimate 4 to 6 weeks of study.

---

### About the Exam

| Detail | Value |
|--------|-------|
| Exam code | DEA-C01 |
| Cost | $300 USD |
| Questions | 65 questions |
| Duration | 130 minutes |
| Passing score | 720 out of 1000 |
| Format | Multiple choice and multiple response |
| Delivery | Online proctored from home via Pearson VUE |
| Valid for | 3 years from passing date |

---

### Exam Domain Breakdown

| Domain | Weight | Topics |
|--------|--------|--------|
| Data Ingestion and Transformation | 34% | Glue, Kinesis, DMS, Kafka MSK, batch vs streaming |
| Storage and Data Management | 26% | S3, Redshift, DynamoDB, RDS, Lake Formation |
| Data Operations and Support | 22% | Athena, QuickSight, Lake Formation, EMR |
| Data Security and Governance | 18% | IAM, KMS, encryption, Lake Formation permissions, audit |

---

### What You Already Know From ClinicalMind

Your project covers these exam topics directly. Do not restudy these from scratch:

- S3 — bucket creation, policies, prefixes, sync, event notifications
- AWS Glue — crawlers, Data Catalog, ETL jobs, PySpark basics
- Amazon Athena — databases, tables, partitioning, query optimization
- IAM — roles, policies, least privilege, cross-service permissions
- AWS CDK — infrastructure as code, deployment
- Lambda — serverless functions, event-driven architecture
- CloudWatch — logs, basic monitoring

---

### What You Need to Learn for the Exam

Study these topics specifically — they are not covered by ClinicalMind:

**Amazon Kinesis — streaming data at scale**
- Kinesis Data Streams — real-time data ingestion, shards, consumers, retention
- Kinesis Data Firehose — delivery to S3, Redshift, OpenSearch without writing consumers
- Kinesis Data Analytics — SQL or Apache Flink on streaming data
- When to use Kinesis vs SQS vs Kafka MSK

**AWS Database Migration Service (DMS)**
- Full load vs CDC (Change Data Capture) migration
- Source and target endpoint configuration
- Replication instances
- Common migration patterns

**Amazon Redshift**
- Column-oriented data warehouse — how it differs from Athena
- Distribution styles — even, key, all
- Sort keys — compound vs interleaved
- Redshift Spectrum — querying S3 from Redshift
- When to use Redshift vs Athena

**AWS Lake Formation**
- What a data lake is and why Lake Formation manages it
- Fine-grained access control — table and column level permissions
- Cross-account data sharing
- Governed tables
- How Lake Formation integrates with Glue, Athena, and Redshift

**Amazon EMR**
- Managed Hadoop and Spark cluster
- When to use EMR vs Glue — EMR is for very large scale or complex Spark, Glue is for simpler ETL
- EMR cluster types — long-running vs transient
- Cost optimization — spot instances for task nodes

**Encryption and Security**
- S3 encryption — SSE-S3, SSE-KMS, SSE-C, client-side
- AWS KMS — customer managed keys, key policies, key rotation
- Glue encryption — metadata and job bookmark encryption
- Athena encryption — query results encryption
- Column-level encryption in Redshift
- VPC endpoints for data services — private connectivity without internet

---

### 4-Week Data Engineer Study Plan

**Week 1 — Kinesis and DMS**

Session prompt: "I am studying for the AWS Data Engineer Associate exam. Read CLINICALMIND_MASTER.md. Teach me Amazon Kinesis from scratch — Data Streams, Firehose, and Data Analytics. Cover shards, consumers, retention, delivery streams, and when I would choose Kinesis over SQS over Kafka MSK. Then cover AWS DMS — full load vs CDC, replication instances, endpoint types. Use data pipeline analogies. Quiz me with 15 questions after."

**Week 2 — Redshift and Lake Formation**

Session prompt: "I am studying for the AWS Data Engineer Associate exam. Read CLINICALMIND_MASTER.md. Teach me Amazon Redshift deeply — column-oriented storage, distribution styles, sort keys, Redshift Spectrum, and when to choose Redshift vs Athena vs EMR. Then teach me AWS Lake Formation — what problems it solves, how fine-grained permissions work, cross-account sharing, and how it integrates with Glue and Athena. Quiz me with 20 questions."

**Week 3 — EMR, Security, and Governance**

Session prompt: "I am studying for the AWS Data Engineer Associate exam. Read CLINICALMIND_MASTER.md. Teach me Amazon EMR — when to use it vs Glue, cluster types, cost optimization with spot instances, and common Spark on EMR patterns. Then go deep on security: all S3 encryption options, KMS key management and rotation, VPC endpoints for data services, and Lake Formation column-level permissions. Quiz me with 20 questions mixing all topics."

**Week 4 — Practice Exam and Weak Area Review**

Session prompt: "I am doing final preparation for the AWS Data Engineer Associate exam. Read CLINICALMIND_MASTER.md. Give me a 65-question practice exam weighted by domain: 22 questions on ingestion and transformation, 17 on storage and management, 14 on operations and support, 12 on security and governance. Present one at a time. Score me, explain every answer, identify my two weakest domains. I will only book the exam when I hit 80% on practice."

---

---

# CERTIFICATIONS INVESTMENT SUMMARY

| Certification | Exam Code | Cost | When | Priority |
|--------------|-----------|------|------|----------|
| AWS Skill Builder badges x5 | free | free | Week 1 of Month 1 | Do first |
| AWS AI Practitioner | AIF-C01 | $150 | End of Month 2 | Must do |
| AWS Data Engineer Associate | DEA-C01 | $300 | 4-6 weeks after Month 3 | Do if budget allows |
| TutorialsDojo practice tests | — | $15 | Month 2 and after | Recommended |

**Minimum investment to complete this course:** $165
**Maximum investment:** $465
**Everything else is free**

---

# FREE RESOURCES — COMPLETE LIST

| Resource | Where to Find | What It Is |
|----------|--------------|------------|
| AWS Skill Builder | skillbuilder.aws | Free courses, labs, and digital badges |
| AWS Educate | aws.amazon.com/education/awseducate | Free credits with university email |
| ExamTopics AIF-C01 | examtopics.com search AIF-C01 | Free AI Practitioner practice questions |
| ExamTopics DEA-C01 | examtopics.com search DEA-C01 | Free Data Engineer practice questions |
| freeCodeCamp AI Practitioner | YouTube search: freeCodeCamp AWS AI Practitioner | Full free video course |
| Andrew Brown Data Engineer | YouTube search: Andrew Brown AWS Data Engineer | Full free video course |
| AWS official sample questions | aws.amazon.com/certification | 20 free official practice questions per exam |
| Synthea patient generator | github.com/synthetichealth/synthea | Fake FHIR patient data |
| AWS Bedrock documentation | docs.aws.amazon.com/bedrock | Official reference docs |
| AWS CDK documentation | docs.aws.amazon.com/cdk | CDK API reference |
| TutorialsDojo DEA practice | tutorialsdojo.com | Best paid practice — $15, worth it |

---

# SKILL BUILDER BADGES — DO IN WEEK 1

Create a free account at skillbuilder.aws. Complete these five courses in Week 1. Each gives a digital badge shareable directly to LinkedIn. This is free and immediate — do it before writing any code.

| Badge | Estimated Time |
|-------|---------------|
| Amazon Bedrock Getting Started | 2 hours |
| Generative AI Essentials on AWS | 3 hours |
| Building Generative AI Apps with Bedrock | 4 hours |
| Prompt Engineering Essentials | 2 hours |
| Responsible AI Essentials | 2 hours |

---

# WHAT YOUR PROFILE LOOKS LIKE AFTER 3 MONTHS

### LinkedIn Headline
Software Engineer | FHIR · HIPAA · EHR | AWS Bedrock & AI Infra | Next.js · CDK | AWS Certified AI Practitioner

### LinkedIn Certifications Section
- AWS Certified AI Practitioner — Amazon Web Services
- AWS Certified Data Engineer Associate — Amazon Web Services
- Amazon Bedrock Getting Started — AWS Skill Builder
- Generative AI Essentials on AWS — AWS Skill Builder
- Building Generative AI Apps with Bedrock — AWS Skill Builder
- Prompt Engineering Essentials — AWS Skill Builder
- Responsible AI Essentials — AWS Skill Builder

### GitHub Pinned Repositories
- clinicalmind — Bedrock Agent, FHIR pipeline, Glue ETL, Athena, CDK, Guardrails
- mcp-server — MCP server for MongoDB
- portfolio — rebuilt Angular 16 portfolio

### LinkedIn Featured Section
- ClinicalMind demo video — 30 second screen recording
- Medium article: I built a HIPAA-ready AI agent on AWS Bedrock
- Portfolio website

### What You Say In Interviews
"I built a clinical AI agent on AWS Bedrock that answers medical questions grounded in FHIR documents — using Knowledge Bases for retrieval, Lambda tools for patient data and drug interaction lookup, and Guardrails for PHI filtering. In Month 3 I added a Glue ETL pipeline that transforms FHIR JSON to Parquet and surfaces clinical analytics via Athena. The agent can now run SQL queries on the data lake on demand. Full stack deployed via AWS CDK. Costs $10 per month to run."

---

# MASTER CHECKLIST

## Month 1 — Build

- [ ] Prerequisites all verified — AWS CLI, Python, Node, CDK, Java, Bedrock access
- [ ] Project scaffolded, git initialized, first commit pushed
- [ ] Bedrock model access enabled for Claude Haiku in us-east-1
- [ ] Skill Builder account created, all 5 badges started
- [ ] hello_bedrock.py runs and returns a response
- [ ] hello_bedrock.ts runs and returns a response
- [ ] compare_apis.py shows both APIs side by side
- [ ] Synthea installed, 100 fake patients generated
- [ ] FHIR files uploaded to S3
- [ ] treatment_protocols.md written with 1000+ words of clinical content
- [ ] Knowledge Base created and synced
- [ ] query_kb.py returns answers with citations
- [ ] Chunking strategy tested and decision documented in ARCHITECTURE.md
- [ ] Bedrock Agent created with correct instruction prompt
- [ ] get_patient_summary Lambda built, deployed, tested directly
- [ ] check_drug_interactions Lambda built with 20+ interactions, deployed, tested
- [ ] Both action groups connected to agent
- [ ] Agent connected to Knowledge Base
- [ ] Agent trace read and understood
- [ ] Guardrail created with PHI masking
- [ ] Topic filter added and tested — off-topic questions refused
- [ ] CDK stack written and cdk synth passes
- [ ] cdk deploy succeeds
- [ ] End-to-end test on deployed stack passes
- [ ] README.md professional and complete
- [ ] ARCHITECTURE.md complete with all decisions
- [ ] All folder READMEs written
- [ ] Demo screenshots taken
- [ ] linkedin-post.md drafted
- [ ] medium-article-outline.md drafted
- [ ] Git tag v1.0.0 created and pushed
- [ ] LinkedIn post published
- [ ] GitHub repo URL added to LinkedIn Featured section

## Month 2 — Certify

- [ ] All 5 Skill Builder badges completed and added to LinkedIn
- [ ] AI Practitioner official course on Skill Builder completed
- [ ] AI and ML fundamentals studied and quizzed
- [ ] Generative AI and foundation models studied and quizzed
- [ ] AWS AI services studied and quizzed
- [ ] Responsible AI and security studied and quizzed
- [ ] Scoring 85%+ on ExamTopics practice consistently
- [ ] Full 50-question practice exam completed with Claude Code
- [ ] Exam booked via Pearson VUE
- [ ] Exam taken and passed
- [ ] Badge downloaded from Credly
- [ ] Certification added to LinkedIn
- [ ] Credly badge shared as LinkedIn post

## Month 3 — Expand

- [ ] Glue Crawler created and run on raw FHIR data
- [ ] Glue Data Catalog populated with discovered schema
- [ ] CDK updated with Glue infrastructure
- [ ] etl/glue_job.py written with PySpark transformation
- [ ] Glue ETL job deployed and run successfully
- [ ] Parquet output verified in S3
- [ ] Second Glue Crawler run on processed Parquet
- [ ] Athena workgroup and database configured
- [ ] All 5 clinical analytics queries written and tested
- [ ] Athena query optimization documented
- [ ] run_clinical_query Lambda built and deployed
- [ ] AnalyticsActions action group added to agent
- [ ] Agent tested with analytics question using real Athena data
- [ ] README.md updated with ETL pipeline and Athena tool
- [ ] ARCHITECTURE.md updated with Month 3 additions
- [ ] Git tag v2.0.0 created and pushed
- [ ] Data Engineer exam domain gaps identified
- [ ] Kinesis studied and quizzed
- [ ] DMS studied and quizzed
- [ ] Redshift studied and quizzed
- [ ] Lake Formation studied and quizzed
- [ ] EMR studied and quizzed
- [ ] Encryption and security studied and quizzed
- [ ] Scoring 80%+ on DEA practice questions
- [ ] Data Engineer exam booked
- [ ] Data Engineer exam taken and passed
- [ ] Second certification added to LinkedIn

---

*Abdulrehman Saleem — DocNow EHR · PUCIT 2024*
*Start date: _______________ Completion target: _______________*
EOF