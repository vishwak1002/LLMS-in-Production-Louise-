

from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
import os

def build_vector_index(docs):
    """
    Build a vector index from the provided documents.
    
    Args:
        docs (list): List of documents to be indexed.
        
    Returns:
        VectorStoreIndex: An index built from the provided documents.
    """
    if not docs:
        raise ValueError("No documents provided for indexing.")
        
   
    Settings.llm = Anthropic(model="claude-3-opus-20240229")
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # Create a node parser and build the vector index
    # Ensure that the documents are in the correct format
    vector_index = VectorStoreIndex.from_documents(docs)
    return vector_index
