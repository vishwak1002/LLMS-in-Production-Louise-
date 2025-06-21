from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from utils.ArticleSummary import ArticleSummary
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
from utils.get_articles import get_articles
 # create prompt template
# notice that we are specifying the "partial_variables" parameter
template = """
You are a very good assistant that summarizes online articles.
 Here's the article you want to summarize.
 ==================
Title: {article_title}
 {article_text}
==================
 {format_instructions}
"""

parser = PydanticOutputParser(pydantic_object=ArticleSummary)
prompt_template = PromptTemplate(
    template=template,
    input_variables=["article_title", "article_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

load_dotenv()
# print(os.environ.get("ANTHROPIC_API_KEY"))    

url = """https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/"""
article = get_articles(url)
if article is None:
    print("Failed to fetch the article.")
else:  
    title, text = article
    # print("Title:", title)
    # print("Text:", text)

model = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)

chain = prompt_template | model | parser

response = chain.invoke({
    "article_title": title,
    "article_text": text
})
# Print the response
print(response)