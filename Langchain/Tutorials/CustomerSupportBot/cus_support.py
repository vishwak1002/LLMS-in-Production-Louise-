
from langchain import PromptTemplate
from utils.utilities import split_text,addToDeepLake
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv
import os

urls = ['https://beebom.com/what-is-nft-explained/',
        'https://beebom.com/how-delete-spotify-account/',
        'https://beebom.com/how-download-gif-twitter/',
        'https://beebom.com/how-use-chatgpt-linux-terminal/',
        'https://beebom.com/how-delete-spotify-account/',
        'https://beebom.com/how-save-instagram-story-with-music/',
        'https://beebom.com/how-install-pip-windows/',
        'https://beebom.com/how-check-disk-usage-linux/']


load_dotenv()
docs =  split_text(urls)
db = addToDeepLake(docs)
query = "how to check disk usage in linux?"
docs = db.similarity_search(query)
print(docs[0].page_content)

template = """You are an exceptional customer support chatbot that gently answer questions.
 You know the following context information.
 {chunks_formatted}
 Answer to the following question from a customer. Use only information from the previous context information. Do not invent stuff.
 Question: {query}
 Answer:"""

prompt = PromptTemplate(
    input_variables=["chunks_formatted", "query"],
    template=template,
)


# user question
query = "How to check disk usage in linux?"
 # retrieve relevant chunks
docs = db.similarity_search(query)
retrieved_chunks = [doc.page_content for doc in docs]
 # format the prompt
chunks_formatted = "\n\n".join(retrieved_chunks)
prompt_formatted = prompt.format(chunks_formatted=chunks_formatted, query=query)
 # generate answer
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
chain = prompt | chat | StrOutputParser()
answer = chain.invoke({"chunks_formatted": chunks_formatted, "query": query})
print("The answer is  : ")
print(answer)
