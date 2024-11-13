import requests
from bs4 import BeautifulSoup

def fetch_google_news(keyword):
    # Format the Google News URL with the specified keyword
    url = f'https://news.google.com/search?q={keyword}%20stock&hl=en-US&gl=US&ceid=US%3Aen'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store the articles
    articles = []
    
    # Find all relevant <a> tags in article sections
    for item in soup.select("article a"):
        title = item.get_text(strip=True)
        link = item.get('href')
        
        # Ensure the link is a valid article link and title has content
        if link and title:
            # Adjust link if it's relative
            if link.startswith('.'):
                link = 'https://news.google.com' + link[1:]
            articles.append({'title': title, 'link': link})

    return articles

# Test with a sample keyword
google_news_data = fetch_google_news("AAPL")
print(google_news_data)
