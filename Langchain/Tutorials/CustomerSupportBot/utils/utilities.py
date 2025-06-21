
from langchain.document_loaders import SeleniumURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import DeepLake

def load_selenium_loader(urls):
    """
    Load the Selenium loader
    """ 
    loader = SeleniumURLLoader(urls=urls)
    return loader


def split_text(urls):
    """
    Split the text into chunks
    """
    loader = load_selenium_loader(urls)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(docs)
    return texts



def get_embedding_function(model_name="all-MiniLM-L6-v2"):
    embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embedding_fn


def addToDeepLake(docs):
    """
    Add documents to Deep Lake dataset
    """
    # create Deep Lake dataset

    my_activeloop_org_id = "vishwak10022000"
    embeddings_fn= get_embedding_function()
    my_activeloop_dataset_name = "langchain_course_customer_support"
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding=embeddings_fn)
 # add documents to our Deep Lake dataset
    db.add_documents(docs)
    return db