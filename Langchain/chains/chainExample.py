from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os
load_dotenv()

model = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)


prompt= "What is a word to replace the following word: {word}?"

prompt_template = PromptTemplate.from_template(prompt)

llm_chain = prompt_template | model | StrOutputParser()

input_list = [
    {"word": "artificial"},
    {"word": "intelligence"},
    {"word": "robot"}
]

input_data = {"word": "happy"}  
response = llm_chain.invoke(input_data)
print(response)

response2= llm_chain.invoke(input_list)
print(response2)