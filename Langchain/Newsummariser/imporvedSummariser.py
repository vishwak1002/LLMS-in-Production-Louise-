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

template = """
As an advanced AI, you've been tasked to summarize online articles into bulleted points. Here are a few examples of how you've done this in the past:
 Example 1:
Original Article: 'The Effects of Climate Change
Summary:
- Climate change is causing a rise in global temperatures.
- This leads to melting ice caps and rising sea levels.
- Resulting in more frequent and severe weather conditions.
 Example 2:
Original Article: 'The Evolution of Artificial Intelligence
Summary:
- Artificial Intelligence (AI) has developed significantly over the past decade.
- AI is now used in multiple fields such as healthcare, finance, and transportation.
- The future of AI is promising but requires careful regulation.
 Now, here's the article you need to summarize:
 ==================
Title: {article_title}
 {article_text}
==================
 Please provide a summarized version of the article in a bulleted list format.
"""

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
response = model.invoke([message])
# Print the response
print("Summary:")
print(response.content)