from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage
from dotenv import load_dotenv
from utils.get_articles import get_articles
import requests
import os
from newspaper import Article

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
  
template ="""You are an advanced AI assistant that summarizes online articles into bulleted lists.
 Here's the article you need to summarize.
 ==================
Title: {article_title}
{article_text}
==================
 Now, provide a summary of the article in bullet points. """
prompt = template.format(article_title=title, article_text=text)
# print(prompt)
# Initialize the Anthropic Chat model
model = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
message = HumanMessage(
    content=prompt
)
# Send the message to the model and get the response
response = model.invoke([message])
# Print the response
print("Summary:")
print(response.content)
