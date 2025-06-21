import os 

from dotenv import load_dotenv

from llama_index import ServiceContext
from llama_index import SimpleDirectoryReader 
from llama_index.vector_stores import DeepLakeVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex

load_dotenv()

claude_model_key = os.environ.get("ANTHROPIC_API_KEY")
active_loop_key = os.environ.get("ACTIVELOOP_TOKEN", None) 


 # load documents
documents = SimpleDirectoryReader("./paul_graham").load_data()


service_context = ServiceContext.from_defaults(chunk_size=512, chunk_overlap=64)
node_parser = service_context.node_parser
nodes = node_parser.get_nodes_from_documents(documents)


my_activeloop_org_id = "vishwak10022000"
my_activeloop_dataset_name = "paulgraham_essays"
dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
vector_store = DeepLakeVectorStore(dataset_path=dataset_path, overwrite=False)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
storage_context.docstore.add_documents(nodes)
vector_index = VectorStoreIndex(nodes, storage_context=storage_context)


query_engine = vector_index.as_query_engine(streaming=True, similarity_top_k=10)
streaming_response = query_engine.query( "What does Paul Graham do?",)
streaming_response.print_response_stream()



from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.query_engine import SubQuestionQueryEngine
query_engine_tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="pg_essay",
            description="Paul Graham essay on What I Worked On",
        ),
    ),
]
query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=query_engine_tools,
    service_context=service_context,
    use_async=True,)

 