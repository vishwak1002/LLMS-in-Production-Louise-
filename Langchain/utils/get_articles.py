
from newspaper import Article
import requests 

def get_articles(url):
    """
    Fetches the article from the given URL and returns its title and text.
    
    Args:
        url (str): The URL of the article to fetch.
        
    Returns:
        tuple: A tuple containing the title and text of the article.
    """
    
    session = requests.Session()
    headers = { 'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.3''',
        } 
    response = session.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
            article = Article(url)
            article.download()
            article.parse()
            return article.title, article.text
    else:
            print(f"Failed to fetch the article. Status code: {response.status_code}")
            return None,None
    
    # Return the title and text
       
   



