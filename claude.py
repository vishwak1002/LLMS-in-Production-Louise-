from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
# print(os.environ.get("ANTHROPIC_API_KEY"))
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
)

english_text = "Hello, how are you?"

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello, Claude! Can you explain what you can do?"}
    ]
)
# Extract the translated text from the response
print(message.content[0].text)
