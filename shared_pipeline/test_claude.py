"""Run this to confirm your Claude API access works.

    python shared_pipeline/test_claude.py
"""
import os
import sys

from dotenv import load_dotenv

load_dotenv()

key = os.getenv("ANTHROPIC_API_KEY")
if not key or key == "your-key-here":
    sys.exit("No ANTHROPIC_API_KEY found. Copy .env.example to .env and add your key.")

from anthropic import Anthropic

model = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")
client = Anthropic(api_key=key)

try:
    msg = client.messages.create(
        model=model,
        max_tokens=100,
        messages=[{"role": "user", "content": "Reply with exactly: API connection works."}],
    )
    print("SUCCESS")
    print("Model:", model)
    print("Response:", msg.content[0].text)
except Exception as e:
    print("FAILED:", type(e).__name__)
    print(e)
    sys.exit(1)
