# Prompt for summarization
from dotenv import load_dotenv
import os
import anthropic


load_dotenv()
# print(os.environ.get("ANTHROPIC_API_KEY"))
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
)
movie = "Toy Story"
prompt = """

Describe the following movie using emojis.
 {movie}: """
 # Few-show examples
examples = [{ "input": "Titanic", "output": "🛳️🌊❤️🧊🎶🔥🚢💔👫??" },{ "input": "The Matrix", "output": "🕶️💊💥👾🔮🌃👨??‍💻🔁🔓??" }]
 # Sending the examples and then asking the question for Toy Story

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": prompt.format(movie=examples[0]["input"])},
        {"role": "assistant", "content": examples[0]["output"]},
        {"role": "user", "content": prompt.format(movie=examples[1]["input"])},
        {"role": "assistant", "content": examples[1]["output"]},
        {"role": "user", "content": prompt.format(movie=movie)},
  ]
)
print(message.content[0].text)

 