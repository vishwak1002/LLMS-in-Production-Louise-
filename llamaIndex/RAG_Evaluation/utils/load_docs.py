

from llama_index.core import SimpleDirectoryReader

def load_documents(path: str):
    """
    Load documents from a specified directory.
    """
    # Specify the path to the directory containing the text files
    # Ensure that the path is correct and accessible
    reader = SimpleDirectoryReader(input_files=["" + path + ""])
    docs = reader.load_data()
    print(f"Loaded {len(docs)} docs")
    return docs

