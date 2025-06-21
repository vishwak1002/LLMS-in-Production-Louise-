from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_anthropic import ChatAnthropic
from utils.vectorStore import db_retriever
import os

from dotenv import load_dotenv
 # create GPT3 wrapper
retriever = db_retriever()

 # create a retrieval chain
load_dotenv()
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
 # create compressor for the retriever
compressor = LLMChainExtractor.from_llm(chat)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
    )

retrieved_docs = compression_retriever.invoke(
 "How Google plans to challenge OpenAI?"
)
print("the response is:")
print(retrieved_docs[0].page_content)

