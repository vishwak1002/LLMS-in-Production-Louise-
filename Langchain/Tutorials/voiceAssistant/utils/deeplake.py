# Define the main function
from utils.get_content import get_documentation_urls,scrape_all_content
from utils.load_docs import load_docs, split_docs
import os
from utils.load_embedding import get_embedding_function
from langchain_community.vectorstores import DeepLake
from langchain_anthropic import ChatAnthropic
from langchain.chains import RetrievalQA


def main():
    base_url = 'https://huggingface.co'
    # Set the name of the file to which the scraped content will be saved
    filename='content.txt'
    # Set the root directory where the content file will be saved
    root_dir ='./'
    relative_urls = get_documentation_urls()
    # Scrape all the content from the relative URLs and save it to the content 
    # file
    content = scrape_all_content(base_url, relative_urls, filename)
    # Load the content from the file
    docs = load_docs(root_dir, filename)
    # Split the content into individual documents
    texts = split_docs(docs)
    # Create a DeepLake database with the given dataset path and embedding 


    db = DeepLake(dataset_path=get_dataset_path(), embedding_function=get_embedding_function())
    # Add the individual documents to the database
    db.add_documents(texts)
    # Clean up by deleting the content file
    os.remove(filename)
 # Call the main function if this script is being run as the main program



# Search the database for a response based on the user's query
def search_db(user_input, db):
    print(user_input)
    retriever = db.as_retriever()
    retriever.search_kwargs['distance_metric'] = 'cos'
    retriever.search_kwargs['fetch_k'] = 100
    retriever.search_kwargs['maximal_marginal_relevance'] = True
    retriever.search_kwargs['k'] = 4
    model =  ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
    )
    qa = RetrievalQA.from_llm(model, retriever=retriever, 
    return_source_documents=True)
    return qa({'query': user_input})

 
def get_dataset_path():
    my_activeloop_org_id = "vishwak10022000"
    my_activeloop_dataset_name = "langchain_course_jarvis_assistant"
    dataset_path= f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    return dataset_path



if __name__ == "__main__":
    main()