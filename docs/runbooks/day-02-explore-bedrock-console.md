# Day 02 — Explore the Bedrock Console

**Course position:** Month 1 · Week 1 · Day 2
**GitHub issue:** #2
**Goal (plain):** Switch on the AI model (Claude Haiku) inside your AWS account, then send it a healthcare question on the AWS website to confirm it works.
**Definition of done:** Claude Haiku responds in the Bedrock playground, and you can explain what input tokens and output tokens mean.

---

## Concepts (simple + examples)

**Foundation model** — a giant, pre-trained AI brain that already learned language. You just use it; you don't train it.
*Example:* like hiring a doctor who already went to medical school — you ask questions, you don't teach them medicine.

**Model tiers (smart vs fast vs cheap)** — Claude comes in tiers:
- **Haiku** — quick, cheapest. ← we use this (keeps the project ~$10/month)
- **Sonnet** — smarter, mid-priced
- **Opus** — top specialist, priciest

Non-Claude options on Bedrock: Amazon **Nova/Titan**, Meta **Llama** — same idea, different makers.

**Playground vs API** — the playground is a chat box on the AWS website for *manual testing by a human*. The API (Days 3–4) is calling the model from *code*.
*Example:* playground = texting the doctor yourself; API = your app texting the doctor automatically.

**Tokens (must be able to explain this)** — the AI breaks text into small chunks called tokens (~¾ of a word). You pay per token, split two ways:
- **Input tokens** = the size of your *question* (what you send in)
- **Output tokens** = the size of the *answer* (what comes back)
*Example:* "What is FHIR?" ≈ 4 input tokens; a 100-word answer ≈ ~130 output tokens. Bill = (input × input price) + (output × output price). This is the core cost lever of the whole project.

---

## Prerequisites

- [ ] AWS CLI configured and working (`aws sts get-caller-identity` returns your account ID)
- [ ] Signed in to the AWS Console in the browser

---

## Steps

### 1. Open AWS in the right region
1. Go to https://console.aws.amazon.com and sign in.
2. Top-right region dropdown → set to **US East (N. Virginia)** = **us-east-1**.
   ⚠️ The whole project lives in `us-east-1`. Wrong region = you won't find the model later.

### 2. Open Bedrock
3. Top search bar → type **Bedrock** → click **Amazon Bedrock**.

### 3. Open the Model catalog
> ⚠️ **The old "Model access" page was RETIRED (seen 2026-07-24).** You no longer manually enable models — serverless models auto-enable on first use. See Gotchas below.

4. Left sidebar → **Model catalog** (under Foundation models).
   (No sidebar? Click the ☰ menu top-left of the Bedrock page.)

### 4. Open Claude Haiku in the playground
5. Find **Claude 3 Haiku** (Anthropic) → click **Open in playground** (or **View model** → open in playground).
6. If a one-time **use-case form** appears (Anthropic, first-time only), fill it simply:
   *"Learning project — clinical Q&A prototype using synthetic data."* → submit.
   The model auto-enables on your first invocation — there is no separate "enable" step or "Access granted" status anymore.

### 5. Test in the playground
7. In the Chat playground with **Claude 3 Haiku** selected, send:
   *"What is FHIR R4 and why does it matter in healthcare?"*
8. Read the answer. Note the **input tokens**, **output tokens**, and **latency** shown near the response.

---

## Verify it worked

- [ ] The playground returns a coherent answer to the FHIR question
- [ ] You can say, in your own words, the difference between input and output tokens

_(The old "Access granted" check is gone — the Model access page was retired.)_

---

## ⚠️ Gotchas & Deviations

_Record anything that differed from the plan, with a date._

- **2026-07-24 — "Model access" page retired by AWS.** The console now shows:
  *"Model access page has been retired. Serverless foundation models are now
  automatically enabled across all AWS commercial regions when first invoked...
  for Anthropic models, first-time users may need to submit use case details."*
  **Impact:** no more manual enable / "Modify model access" / "Access granted".
  **New flow:** Model catalog → open Claude Haiku in playground → fill the
  one-time Anthropic use-case form if prompted → invoke. Steps 3–5 above were
  rewritten to match. Marketplace-served models need one invocation by a user
  with AWS Marketplace permissions to enable account-wide.
