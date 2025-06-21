from dotenv import load_dotenv
import os
from openai import OpenAI



load_dotenv()


english_text = "Hello, how are you?"
# Set up OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
# Function to translate text using OpenAI's GPT-3.5  
#    
response =  client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Translate the following English text to French: {english_text}"}
    ]
)

# Extract the translated text from the response 
translated_text = response['choices'][0]['message']['content']
print(f"Translated text: {translated_text}")