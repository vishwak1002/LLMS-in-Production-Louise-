from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.output_parsers import StructuredOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
# print(os.environ.get("ANTHROPIC_API_KEY"))
prompt = PromptTemplate( template= " Question: {question} \n Answer : ", input_variables=["question"])
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
# Create a chain with the prompt and the LLM
# chain = LLMChain(
#     llm=chat,
#     prompt=prompt,
# ) deprecated
# Run the chain with a question

chain = chat | prompt 
question = "What is the capital of France?"
response = chain.invoke(question)
# Print the response
print(response)