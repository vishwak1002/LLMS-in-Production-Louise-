

from llama_index.core.evaluation import generate_question_context_pairs
from llama_index.llms.anthropic import Anthropic

def generate_questions(nodes):
    llm = Anthropic(model="claude-3-opus-20240229")
    qa_dataset = generate_question_context_pairs(
        nodes=nodes,
        llm=llm,
        num_questions_per_chunk=2
    )
    queries = list(qa_dataset.queries.values())
    print(queries[0:10])
    return qa_dataset