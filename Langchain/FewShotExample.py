from langchain.prompts import FewShotPromptTemplate ,PromptTemplate
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.output_parsers import StrOutputParser 
# print(os.environ.get("ANTHROPIC_API_KEY"))
prompt = PromptTemplate( template= " Question: {question} \n Answer : ", input_variables=["question"])
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)


examples = [
    {
        "query": "How do I become a better programmer?",
        "answer": "Try talking to a rubber duck; it works wonders."

 }, {
        "query": "Why is the sky blue?",
        "answer": "It's nature's way of preventing eye strain."
    }
]
example_template = """ 
User: {query}
AI: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)


prefix = """The following are excerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative and funny responses to users' questions. Here are some
examples:
"""
suffix = """
User: {query}
AI: """

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n"
) 

chain = chat | StrOutputParser()
example_prompt =  few_shot_prompt_template.format(query="How do I learn quantum computing?")
# input_data = {"query": "How can I learn quantum computing?"}
response = chain.invoke(example_prompt)
# Print the response        
print(response)