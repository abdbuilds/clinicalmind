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

### 3. Go to Model access
4. Left sidebar → scroll to the bottom → under **Bedrock configurations**, click **Model access**.
   (No sidebar? Click the ☰ menu top-left of the Bedrock page.)

### 4. Enable Claude Haiku
5. Click **Modify model access** (or **Enable specific models** on first use).
6. Find **Anthropic** → tick **Claude 3 Haiku** (may just say **Claude Haiku**).
7. Click **Next**.
8. If a **use-case form** appears, fill it simply: *"Learning project — clinical Q&A prototype using synthetic data."* Submit.
9. Click **Submit** / **Save changes**.

### 5. Wait for access
10. Back on the Model access list, Claude Haiku status becomes **Access granted** (usually instant, can take a few minutes).

### 6. Test in the playground
11. Left sidebar → **Playgrounds** → **Chat** (or **Chat / Text**).
12. Select model → **Anthropic** → **Claude 3 Haiku**.
13. Send: *"What is FHIR R4 and why does it matter in healthcare?"*
14. Read the answer. Note the **input tokens**, **output tokens**, and **latency** shown near the response.

---

## Verify it worked

- [ ] Claude Haiku shows **Access granted** in Model access
- [ ] The playground returns a coherent answer to the FHIR question
- [ ] You can say, in your own words, the difference between input and output tokens

---

## ⚠️ Gotchas & Deviations

_Record anything that differed from the plan, with a date. Empty is fine._

- _(none yet — will fill in during execution if AWS's screens differ or an extra step is needed)_
