from langchain.text_splitter import RecursiveCharacterTextSplitter



def get_text_splitter():
    """
    Get the text splitter
    """
    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000, chunk_overlap=0, separators=[" ", ",", "\n"]
   )
    return text_splitter


def split_text(text):
    """
    Split the text into chunks
    """
    text_splitter = get_text_splitter()
    texts = text_splitter.split_text(text)
    return texts

