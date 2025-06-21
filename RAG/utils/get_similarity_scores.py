

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .embedding import get_embedding

def get_similarity_scores(df, query):
    query_emb = get_embedding(query)
    if query_emb is None:
        return None
    cosine_similarities = cosine_similarity([query_emb], df['embeddings'].tolist())
    return cosine_similarities

def get_top_n_similar_chunks(df, query, n=3):
    cosine_similarities = get_similarity_scores(df, query)
    if cosine_similarities is None:
        return None
    top_n_indices = np.argsort(cosine_similarities[0])[::-1][:n]
    top_n_chunks = df.iloc[top_n_indices]
    return top_n_chunks
