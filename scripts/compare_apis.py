"""
compare_apis.py — Anthropic API vs Amazon Bedrock, side by side (ClinicalMind, Day 5).

Sends the SAME prompt to Claude Haiku 4.5 two ways:
  1. Amazon Bedrock (boto3)         — always runs (uses your ~/.aws creds)
  2. Anthropic API directly (SDK)   — runs only if ANTHROPIC_API_KEY is set

Prints each answer, its latency, and its token usage so you can compare.

Run:
    source .venv/bin/activate
    python3 scripts/compare_apis.py
"""

import json
import os
import time

import boto3
from botocore.exceptions import ClientError

PROMPT = "In 3 sentences, explain what FHIR R4 is and why it matters in healthcare."
MAX_TOKENS = 300

REGION = os.environ.get("AWS_REGION", "us-east-1")
BEDROCK_MODEL_ID = os.environ.get(
    "BEDROCK_MODEL_ID", "us.anthropic.claude-haiku-4-5-20251001-v1:0"
)
# Anthropic's direct API uses the plain model alias (no us. prefix, no version):
ANTHROPIC_MODEL_ID = os.environ.get("ANTHROPIC_MODEL_ID", "claude-haiku-4-5")


def call_bedrock() -> dict:
    """Call Claude Haiku 4.5 via Amazon Bedrock. Returns timing + usage + text."""
    client = boto3.client("bedrock-runtime", region_name=REGION)
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": MAX_TOKENS,
        "messages": [{"role": "user", "content": PROMPT}],
    }
    start = time.perf_counter()
    resp = client.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    result = json.loads(resp["body"].read())
    text = "".join(b["text"] for b in result.get("content", []) if b.get("type") == "text")
    usage = result.get("usage", {})
    return {
        "text": text,
        "latency_ms": round(elapsed_ms),
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
    }


def call_anthropic() -> dict | None:
    """Call Claude Haiku 4.5 via Anthropic's API directly. None if no API key."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    from anthropic import Anthropic  # imported lazily so the script runs without the key

    client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    start = time.perf_counter()
    msg = client.messages.create(
        model=ANTHROPIC_MODEL_ID,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": PROMPT}],
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    text = "".join(b.text for b in msg.content if b.type == "text")
    return {
        "text": text,
        "latency_ms": round(elapsed_ms),
        "input_tokens": msg.usage.input_tokens,
        "output_tokens": msg.usage.output_tokens,
    }


def show(title: str, r: dict) -> None:
    print(f"\n===== {title} =====")
    print(r["text"])
    print(f"[latency: {r['latency_ms']} ms | input: {r['input_tokens']} | output: {r['output_tokens']}]")


def main() -> None:
    print(f"Prompt: {PROMPT}\n" + "=" * 60)

    # 1. Bedrock (always)
    try:
        show("AMAZON BEDROCK (boto3)", call_bedrock())
    except ClientError as err:
        print(f"\nBedrock failed: {err.response['Error']['Message']}")

    # 2. Anthropic direct (optional)
    anthropic_result = call_anthropic()
    if anthropic_result is None:
        print("\n===== ANTHROPIC API (direct) =====")
        print("SKIPPED — no ANTHROPIC_API_KEY set.")
        print("Set one (export ANTHROPIC_API_KEY=sk-ant-...) to run this side too.")
    else:
        show("ANTHROPIC API (direct)", anthropic_result)


if __name__ == "__main__":
    main()
