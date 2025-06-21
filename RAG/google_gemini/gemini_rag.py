import google.generativeai as genai 
import sys
import os
import pandas as pd
# Add project root (RAG/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.load_file import convert_to_pandas_dataframe
from utils.embedding import generate_embeddings_from_dataFrame
from utils.get_similarity_scores import get_top_n_similar_chunks
from googleAccess import load_creds



def print_RAG_gemini():

    try:
        system_prompt =  "You are an assistant and expert in answering questions from a chunks of content. Only answer AI-related question, else say that you cannot answer this question."
 # Create a user prompt with the user's question
        prompt = (
     "Read the following informations that might contain the context you require to answer the question. You can use the informations starting from the <START_OF_CONTEXT> tag and end with the <END_OF_CONTEXT> tag. Here is the content:\n\n<START_OF_CONTEXT>\n{}\n<END_OF_CONTEXT>\n\n"
     "Please provide an informative and accurate answer to the following question based on the avaiable context. Be concise and take your time. \nQuestion: {}\nAnswer:"
    )
 # Add the retrieved pieces of text to the prompt
 # .
        emb_file_path = "../RAG/embeddings.pkl"
        if  os.path.exists(emb_file_path):
            df = pd.read_pickle(emb_file_path)
        else:
            file_path = "../RAG/mini-llama-articles.csv"
            df = convert_to_pandas_dataframe(file_path) 
            df = generate_embeddings_from_dataFrame(df)
            df.to_pickle(emb_file_path)

    # Assuming you have a function to get the top N similar chunks
        QUESTION = "How many parameters LLaMA 3.1 model has?"
        top_n_chunks = get_top_n_similar_chunks(df, QUESTION, n=3)
        prompt = prompt.format("".join(top_n_chunks), QUESTION)
        creds = load_creds()
        genai.configure(credentials=creds)
        model = genai.GenerativeModel(model_name= "gemini-1.5-flash", system_instruction=system_prompt)
        result = model.generate_content(prompt,request_options={"timeout": 1000},)
        print(result)
        res = result.text
        print(res)
    except Exception as e:
        print(f"An error occurred: {e}")


 

if __name__ == "__main__":
    print_RAG_gemini()
    