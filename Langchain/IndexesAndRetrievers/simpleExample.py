from langchain_community.document_loaders import TextLoader
from utils.vectorStore import addToDeepLake,db_retriever
from langchain.chains import RetrievalQA
from langchain_anthropic import ChatAnthropic
from langchain.llms import OpenAI
import os

from dotenv import load_dotenv
 # text to write to a local file
# taken from https://www.theverge.com/2023/3/14/23639313/google-ai-language-model-palm-api-challenge-openai
text =""" Google opens up its AI language model PaLM to challenge OpenAI and GPT-3 Google offers developers access to one of its most advanced AI language models: PaLM. The search giant is launching an API for PaLM alongside a number of AI enterprise tools it says will help businesses "generate text, images, code, videos, audio, and more from simple natural language prompts."
 PaLM is a large language model, or LLM, similar to the GPT series created by OpenAI or Meta's Llama family of models. Google first announced PaLM in April 2022. Like other LLMs, PaLM is a flexible system that can potentially carry out all sorts of text generation and editing tasks. You could train PaLM to be a conversational chatbot like ChatGPT, for example, or you could use it for tasks like summarizing text or even writing code. (It's similar to features Google also announced today for its Workspace apps like Google Docs and Gmail.)
"""
 # write text to local file
with open("my_file.txt", "w") as file:
    file.write(text)
 # use TextLoader to load text from local file
loader = TextLoader("my_file.txt")
docs_from_file = loader.load()
print(len(docs_from_file))

from langchain.text_splitter import CharacterTextSplitter
 # create a text splitter
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
 # split documents into chunks
docs = text_splitter.split_documents(docs_from_file)
print(len(docs))

# addToDeepLake(docs=docs)

retriever = db_retriever()

 # create a retrieval chain
load_dotenv()
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
qa_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever
)

query = "How Google plans to challenge OpenAI?"
response = qa_chain.run(query)
print("the response is:")
print(response)
