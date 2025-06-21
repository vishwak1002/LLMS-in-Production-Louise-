from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
from langchain.chains.base import Chain
from typing import Dict,List

 

load_dotenv()

llm = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)


