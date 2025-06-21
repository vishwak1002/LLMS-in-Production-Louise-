import os

import anthropic
from dotenv import load_dotenv
load_dotenv()
# Anthropic API key
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
# Anthropic API client  