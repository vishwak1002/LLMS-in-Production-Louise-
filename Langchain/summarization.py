from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
import os
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()
# print(os.environ.get("ANTHROPIC_API_KEY"))
template = "You are an AI Assistant that helps users find information about movies."
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)

document_loader = PyPDFLoader("./dummy.pdf")
documents = document_loader.load()

#summarize the document 
chain = load_summarize_chain(
    chat
)
summary = chain.invoke(documents)
# Print the summary
print(summary['output_text'])