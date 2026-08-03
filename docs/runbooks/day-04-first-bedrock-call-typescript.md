# Day 04 — First Bedrock API Call in TypeScript

**Course position:** Month 1 · Week 1 · Day 4
**GitHub issue:** #4
**Goal (plain):** Same call as Day 3, but in TypeScript using the AWS SDK v3.
**Definition of done:** `npx tsx scripts/hello_bedrock.ts` prints a coherent answer from Claude Haiku 4.5.

---

## Concepts (simple + examples) — what's different from Python

- **Client + command pattern (SDK v3):** build a command, then send it.
  `const cmd = new InvokeModelCommand({...}); await client.send(cmd);`
  (Python called the method directly; TS separates "the request" from "sending it".)
- **Type safety:** `InvokeModelCommand` has typed inputs — the editor catches typos.
- **async/await required:** Bedrock calls are asynchronous; wrap in an `async main()`.
- **Same everything else:** same `~/.aws` credentials, region, model id, request body.

---

## Prerequisites

- [ ] Node 18+ and npm (Day 1)
- [ ] Claude Haiku 4.5 usable (Day 2)

---

## Steps

1. `package.json` at repo root (metadata + a `hello:ts` script).
2. `tsconfig.json` (CommonJS, ES2020, strict).
3. Install deps:
   ```bash
   npm install @aws-sdk/client-bedrock-runtime
   npm install -D typescript tsx @types/node
   ```
4. Write `scripts/hello_bedrock.ts` (client + `InvokeModelCommand` + `client.send`).
5. Run:
   ```bash
   npx tsx scripts/hello_bedrock.ts     # or: npm run hello:ts
   ```

---

## Verify it worked

- [ ] Prints a coherent FHIR-resources answer from Claude Haiku 4.5
- [ ] Prints exact input/output token counts

---

## ⚠️ Gotchas & Deviations

- **2026-08-04 — `ts-node` crashes with TypeScript 7.** The course suggested
  `ts-node`, but npm installed the just-released **TypeScript 7**, which ts-node
  10.9.2 doesn't support yet — it fails at startup with
  `TypeError: Cannot read properties of undefined (reading 'fileExists')`.
  **Fix:** use **`tsx`** instead (`npm i -D tsx`, then `npx tsx <file>`). tsx is
  the modern, faster TS runner and works with new Node + TS. Updated the
  `hello:ts` npm script to use tsx. Verified working 2026-08-04.
- Same inference-profile id note as Day 3: use `us.anthropic.claude-haiku-4-5-20251001-v1:0`.
