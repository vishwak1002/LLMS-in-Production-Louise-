# Define a function to load documents from a file

from langchain.document_loaders import TextLoader
import os
from langchain.text_splitter import CharacterTextSplitter

def load_docs(root_dir, filename):
    # Create an empty list to hold the documents
    docs = []
    try:
        # Load the file using the TextLoader class and UTF-8 encoding
        loader = TextLoader(os.path.join(
            root_dir, filename), encoding='utf-8')
        # Split the loaded file into separate documents and add them to the list 
        # of documents
        docs.extend(loader.load_and_split())
    except Exception as e:
        # If an error occurs during loading, ignore it and return an empty list 
        # of documents
        pass
    # Return the list of documents
    return docs

def split_docs(docs):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_documents(docs)