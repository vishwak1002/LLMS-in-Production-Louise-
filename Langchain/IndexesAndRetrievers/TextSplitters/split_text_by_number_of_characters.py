from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("./dummy.pdf")
pages = loader.load_and_split()
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
texts = text_splitter.split_documents(pages)
print(texts[0])
print (f"You have {len(texts)} documents")
print ("Preview:")
print (texts[0].page_content)
print(texts[1].page_content)


# NLTK Splitter
import nltk
nltk.download('punkt_tab')
from langchain.text_splitter import NLTKTextSplitter
nltk_splitter = NLTKTextSplitter(chunk_size=1000, chunk_overlap=20)
texts = nltk_splitter.split_documents(pages)
print (f"You have {len(texts)} documents")
print ("Preview:")
print (texts[0].page_content)
print("Preview 2 :")
print(texts[1].page_content)
