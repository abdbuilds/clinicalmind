"""
hello_bedrock.py — first Bedrock API call in Python (ClinicalMind, Day 3).

Asks Claude Haiku 4.5 (via Amazon Bedrock) a healthcare question and prints
the answer plus the exact token usage.

Run:
    source .venv/bin/activate         # turn on the project's Python box
    python3 scripts/hello_bedrock.py
"""

import json
import os
import sys

import boto3
from botocore.exceptions import ClientError

# --- Config (override via environment variables if you like) -----------------
# Region where Bedrock runs. Set on Day 1; defaults to us-east-1.
REGION = os.environ.get("AWS_REGION", "us-east-1")

# The model to call. Claude 4.x on Bedrock must be called via a cross-region
# "inference profile" id (the `us.` prefix), NOT the bare model id.
MODEL_ID = os.environ.get(
    "BEDROCK_MODEL_ID", "us.anthropic.claude-haiku-4-5-20251001-v1:0"
)

# The healthcare question we send.
QUESTION = "What are the most important FHIR R4 resource types for an EHR system?"


def main() -> None:
    # 1. Create the client for CALLING models. Credentials come automatically
    #    from your `aws configure` setup — never hard-code keys.
    client = boto3.client("bedrock-runtime", region_name=REGION)

    # 2. Build the request body. Claude on Bedrock uses Anthropic's Messages
    #    format, wrapped with the Bedrock `anthropic_version` tag.
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,  # hard cap on the answer length (and cost)
        "messages": [
            {"role": "user", "content": QUESTION},
        ],
    }

    # 3. Send it. invoke_model does one request → one response.
    try:
        response = client.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json",
        )
    except ClientError as err:
        code = err.response["Error"]["Code"]
        print(f"\n❌ Bedrock call failed ({code}): {err.response['Error']['Message']}")
        if code in ("AccessDeniedException", "ResourceNotFoundException"):
            print(
                "→ Likely the model isn't enabled in this account/region, or the "
                "model id is wrong. Open Claude Haiku 4.5 once in the Bedrock "
                "playground to enable it, and confirm AWS_REGION is us-east-1."
            )
        sys.exit(1)

    # 4. Parse the response. The body is a stream of JSON bytes.
    result = json.loads(response["body"].read())

    # The answer text lives in result["content"] (a list of blocks).
    answer = "".join(
        block["text"] for block in result.get("content", []) if block.get("type") == "text"
    )

    # 5. Show the answer and the EXACT token counts (the real, billed numbers).
    usage = result.get("usage", {})
    print("\n=== Question ===")
    print(QUESTION)
    print("\n=== Claude Haiku 4.5 says ===")
    print(answer)
    print("\n=== Tokens (exact) ===")
    print(f"input:  {usage.get('input_tokens')}")
    print(f"output: {usage.get('output_tokens')}")


if __name__ == "__main__":
    main()
