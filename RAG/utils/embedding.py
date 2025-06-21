from openai import OpenAI
import os
from tqdm.notebook import tqdm
import pandas as pd
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()



def get_embedding(text, model="text-embedding-3-small"):
    try :
        text = text.replace("\n", " ")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embedding = model.encode(text)
        return embedding

    except Exception as e:
        print(f"Error in get_embedding: {e}")
        return None

def generate_embeddings_from_dataFrame(df):
    embeddings =[]
    for index, row in tqdm(df.iterrows()):
        print(index)
        embedding = get_embedding(row['chunk'])
        if embedding is not None:
            embeddings.append(embedding)
    embeddings_values=pd.Series(embeddings)
    df.insert(loc=1, column='embeddings', value=embeddings_values)
    print(df)
    return df
