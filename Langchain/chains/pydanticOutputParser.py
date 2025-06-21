
from langchain.output_parsers import PydanticOutputParser,CommaSeparatedListOutputParser
from pydantic import BaseModel, Field, field_validator
from typing import List
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

 # Define your desired data structure.
class Suggestions(BaseModel):
    words: List[str] = Field(description="""list of substitue words based on context""")
     # Throw error in case of receiving a numbered-list from API
    @field_validator('words')
    def not_start_with_number(cls, field):
        for item in field:
            if item[0].isnumeric():
                raise ValueError("The word can not start with numbers!")
        return field

parser = PydanticOutputParser(pydantic_object=Suggestions)

parser2 = CommaSeparatedListOutputParser()


template = """
Offer a list of suggestions to substitue the specified target_word based \
the presented context.
{format_instructions}
target_word={target_word}
context={context}
"""
target_word = "behaviour"
context = """The behaviour of the students in the classroom was disruptive and made it difficult for the teacher to conduct the lesson."""
prompt_template = PromptTemplate(
    template=template,
    input_variables=["target_word", "context"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)




load_dotenv()

llm = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)


chain = prompt_template | llm | parser

response = chain.invoke({
    "target_word": target_word,
    "context": context
})
# Print the response        
print(response)



prompt_template2 = PromptTemplate(
    template=template,
    input_variables=["target_word", "context"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

chain2 = prompt_template | llm | parser2
response2 = chain2.invoke({
    "target_word": target_word,
    "context": context
})
# Print the response
print(response2)