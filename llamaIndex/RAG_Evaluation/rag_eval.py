

from utils.build_vector_index import build_vector_index
from utils.load_docs import load_documents
from utils.generate_questions import generate_questions
from utils.eval_retreive import get_results
from dotenv import load_dotenv
import asyncio




load_dotenv()
docs = load_documents("./venus_transmission.txt")
vector_index = build_vector_index(docs)
query_engine = vector_index.as_query_engine()
response = query_engine.query("What was the first beings to inhabit the planet")


nodes = list(vector_index.docstore.docs.values())
queries = generate_questions(nodes)


result = asyncio.run(get_results(vector_index, queries))
print(result)
 



# print(response.response)
# print(response.source_nodes[0].get_text())
# print("The difference between the first and second source nodes:")
# print(response.source_nodes[1].get_text())

