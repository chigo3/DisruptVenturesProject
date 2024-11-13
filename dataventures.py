import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from transformers import pipeline
import yfinance as yf

# Define the Hugging Face sentiment model globally to avoid reloading it for each call
sentiment_model = pipeline("sentiment-analysis")

def fetch_articles(keyword):
    url = f'https://news.google.com/search?q={keyword}%20stock&hl=en-US&gl=US&ceid=US%3Aen'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.find_all('article'):
        title = item.find('h3').text if item.find('h3') else 'No title'
        link = item.find('a')['href'] if item.find('a') else 'No link'
        articles.append({'keyword': keyword, 'title': title, 'link': f'https://news.google.com{link}'})
    
    return articles

# Define a function to fetch data for a given stock ticker
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    history = stock.history(period="5d")  # Last 5 days of stock data

    # Fetch recent news (headlines only)
    news = stock.news[:5]  # Limit to top 5 news items
    
    # Structure data
    data = {
        'ticker': ticker,
        'price': info.get('currentPrice', 'N/A'),
        'previousClose': info.get('previousClose', 'N/A'),
        'marketCap': info.get('marketCap', 'N/A'),
        'news': [{'title': item['title'], 'link': item['link']} for item in news]
    }

    return data

def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower()

def analyze_sentiment(text):
    result = sentiment_model(text)
    return result[0]['label']

def main(stock_keywords, num_articles=5):
    all_articles = []
    for keyword in stock_keywords:
        articles = fetch_articles(keyword)[:num_articles]  # Limit number of articles per stock
        for article in articles:
            article['cleaned_title'] = preprocess_text(article['title'])
            article['sentiment'] = analyze_sentiment(article['cleaned_title'])
            all_articles.append(article)
    
    df = pd.DataFrame(all_articles)
    print(df.head())  # Display first few rows to verify output

    # Optionally, save to CSV or JSON for later use
    df.to_csv("scraped_articles_with_sentiment.csv", index=False)
    return df

if __name__ == "__main__":
    stock_keywords = ['AAPL', 'MSFT', 'NVDA']
    main(stock_keywords, num_articles=5)  # Adjust number of articles if needed