

import os
import re
import requests
from bs4 import BeautifulSoup
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter

def get_documentation_urls():
    # List of relative URLs for Hugging Face documentation pages, 
    # commented a lot of these because it would take too long to scrape 
    # all of them
    return [
            '/docs/huggingface_hub/guides/overview',
            '/docs/huggingface_hub/guides/download',
            '/docs/huggingface_hub/guides/upload',
            '/docs/huggingface_hub/guides/hf_file_system',
            '/docs/huggingface_hub/guides/repository',
            '/docs/huggingface_hub/guides/search',
            # You may add additional URLs here or replace all of them
    ]
def construct_full_url(base_url, relative_url):
    # Construct the full URL by appending the relative URL to the base URL
    return base_url + relative_url

def scrape_page_content(url):
    # Send a GET request to the URL and parse the HTML response using 
    # BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract the desired content from the page (in this case, the body text)
    text=soup.body.text.strip()
    # Remove non-ASCII characters
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\xff]', '', text)
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def scrape_all_content(base_url, relative_urls, filename):
    # Loop through the list of URLs, scrape content and add it to the 
    # content list
    content = []
    for relative_url in relative_urls:
        full_url = construct_full_url(base_url, relative_url)
        scraped_content = scrape_page_content(full_url)
        content.append(scraped_content.rstrip('\n'))
     # Write the scraped content to a file
    with open(filename, 'w', encoding='utf-8') as file:
        for item in content:
            file.write("%s\n" % item)
    return content
