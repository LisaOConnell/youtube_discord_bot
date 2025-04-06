import os
from dotenv import load_dotenv
import requests

load_dotenv()
webhook = os.getenv("DISCORD_WEBHOOK")

# Send a test message
message = "✅ Bot test successful! If you see this, the webhook is working."
requests.post(webhook, json={"content": message})