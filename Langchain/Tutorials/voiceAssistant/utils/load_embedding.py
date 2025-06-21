from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import DeepLake

def load_embeddings_and_database(active_loop_data_set_path):
    db = DeepLake(
        dataset_path=active_loop_data_set_path,
        read_only=True,
        embedding_function=get_embedding_function(),
    )
    return db



def get_embedding_function(model_name="all-MiniLM-L6-v2"):
    embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embedding_fn