/**
 * hello_bedrock.ts — first Bedrock API call in TypeScript (ClinicalMind, Day 4).
 *
 * Same job as hello_bedrock.py, but with the AWS SDK v3 (client + command pattern).
 *
 * Run:
 *   npx ts-node scripts/hello_bedrock.ts
 */

import {
  BedrockRuntimeClient,
  InvokeModelCommand,
} from "@aws-sdk/client-bedrock-runtime";

// --- Config (override via environment variables if you like) -----------------
const REGION = process.env.AWS_REGION ?? "us-east-1";

// Claude 4.x on Bedrock must use the cross-region inference-profile id (us. prefix).
const MODEL_ID =
  process.env.BEDROCK_MODEL_ID ??
  "us.anthropic.claude-haiku-4-5-20251001-v1:0";

const QUESTION =
  "What are the most important FHIR R4 resource types for an EHR system?";

async function main(): Promise<void> {
  // 1. Create the client. Credentials come automatically from ~/.aws (never hard-coded).
  const client = new BedrockRuntimeClient({ region: REGION });

  // 2. Build the request body (Anthropic Messages format, wrapped for Bedrock).
  const body = {
    anthropic_version: "bedrock-2023-05-31",
    max_tokens: 512,
    messages: [{ role: "user", content: QUESTION }],
  };

  // 3. Build the command, then send it (the SDK v3 "client + command" pattern).
  const command = new InvokeModelCommand({
    modelId: MODEL_ID,
    contentType: "application/json",
    accept: "application/json",
    body: JSON.stringify(body),
  });

  const response = await client.send(command);

  // 4. Parse the response. body is raw bytes -> decode -> JSON.
  const result = JSON.parse(new TextDecoder().decode(response.body));

  // 5. Pull out the text and the exact token usage.
  const answer = (result.content ?? [])
    .filter((block: { type: string }) => block.type === "text")
    .map((block: { text: string }) => block.text)
    .join("");

  console.log("\n=== Question ===");
  console.log(QUESTION);
  console.log("\n=== Claude Haiku 4.5 says ===");
  console.log(answer);
  console.log("\n=== Tokens (exact) ===");
  console.log(`input:  ${result.usage?.input_tokens}`);
  console.log(`output: ${result.usage?.output_tokens}`);
}

main().catch((err) => {
  console.error("\n❌ Bedrock call failed:", err.name, "-", err.message);
  console.error(
    "→ If access/not-found: open Claude Haiku 4.5 once in the Bedrock playground, " +
      "and check AWS_REGION is us-east-1 and the model id is the us. inference profile.",
  );
  process.exit(1);
});
