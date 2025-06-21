from langchain_anthropic import ChatAnthropic
from langchain.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate

from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
# print(os.environ.get("ANTHROPIC_API_KEY"))
template = "You are an AI Assistant that helps users find information about movies."
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
# Define the system message
system_message = SystemMessagePromptTemplate.from_template(template)
# Define the human message
human_template = "Find  information about movie {movie_title}"
human_message = HumanMessagePromptTemplate.from_template(human_template)
# Create the chat prompt template   
chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
# Create the final prompt
response = chat.invoke(chat_prompt.format_prompt(movie_title="Inception").to_messages())
# Extract the translated text from the response
print(response.content)
