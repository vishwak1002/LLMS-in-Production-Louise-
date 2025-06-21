from langchain_community.vectorstores import DeepLake
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
# load environment variables from .env file
load_dotenv()
 # Before executing the following code, make sure to have your
# Activeloop key saved in the "ACTIVELOOP_TOKEN" environment variable.
 # create Deep Lake dataset
# TODO: use your organization id here. (by default, org id is your username)
def addToDeepLake(docs):
    """
    Add documents to Deep Lake dataset
    """
    # create Deep Lake dataset

    my_activeloop_org_id = "vishwak10022000"
    embeddings_fn= get_embedding_function()
    my_activeloop_dataset_name = "langchain_course_indexers_retrievers"
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding=embeddings_fn)
 # add documents to our Deep Lake dataset
    db.add_documents(docs)



def get_embedding_function(model_name="all-MiniLM-L6-v2"):
    embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embedding_fn
    

def db_retriever():
    """
    Create a retriever from Deep Lake dataset
    """
    my_activeloop_org_id = "vishwak10022000"
    embeddings_fn= get_embedding_function()
    my_activeloop_dataset_name = "langchain_course_indexers_retrievers"
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding=embeddings_fn)
    return db.as_retriever()