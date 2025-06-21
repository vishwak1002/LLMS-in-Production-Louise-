import os
from llama_index.postprocessor.cohere_rerank import CohereRerank

cohere_rerank = CohereRerank(api_key=os.environ['COHERE_API_KEY'], top_n=2)


query_engine = vector_index.as_query_engine(
    similarity_top_k=10,
    node_postprocessors=[cohere_rerank],
)


response = query_engine.query( "What did Sam Altman do in this essay?")
print(response)
