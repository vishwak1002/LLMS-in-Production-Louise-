
from utils.utilities import download_mp4_from_youtube,get_transcried_text,save_transcribed_text_to_file
from utils.split_text import split_text
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
import textwrap
from dotenv import load_dotenv
import os


filename = "video.mp4"
url = "https://www.youtube.com/watch?v=mBjPyte2ZZo"
download_mp4_from_youtube(url,filename=filename)
text = get_transcried_text(filename=filename)
load_dotenv()
save_transcribed_text_to_file(text,"transcribed_text.txt")


with open('transcribed_text.txt') as f:
    text = f.read()
split_texts = split_text(text)
chat = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)
docs = [Document(page_content=t) for t in split_texts[:4]]
chain = load_summarize_chain(chat,chain_type="map_reduce")
output = chain.run(docs)
wrapped_text = textwrap.fill(output,width=100)
print(wrapped_text)

prompt_template = """Write a concise bullet point summary of the following:
 {text}
 CONSCISE SUMMARY IN BULLET POINTS:"""
BULLET_POINT_PROMPT = PromptTemplate(template=prompt_template, 
                        input_variables=["text"])
chain = load_summarize_chain(chat, 
                             chain_type="stuff", 
                             prompt=BULLET_POINT_PROMPT)
output_summary = chain.run(docs)
wrapped_text = textwrap.fill(output_summary, 
                             width=1000,
                             break_long_words=False,
                             replace_whitespace=False)
print(wrapped_text)



#TODO do it for miltiple videos with a Embedding database