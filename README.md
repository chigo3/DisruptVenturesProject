# Sentiment-Based Stocks Tracker for Beginner Investors

We aim to create a user-friendly platform for tracking and analyzing stocks using sentiment analysis. This platform aggregates financial news and social media mentions of various stocks and provides sentiment-based insights to guide beginner investors.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
---

## Introduction

This project aims to provide beginner investors with insights into stock trends by analyzing sentiment from news articles. The sentiment-based recommendations feature allows users to track stocks with positive, negative, or neutral sentiment trends and receive alerts for significant sentiment shifts.

## Features

- **Sentiment Analysis**: Uses NLP models to analyze the sentiment (positive, negative, neutral) of news articles related to specific stocks.
- **Data Aggregation**: Scrapes news from Yahoo Finance and Google News, consolidating relevant information in a single interface.
- **Stock Watchlist**: Users can maintain a list of stocks to track and receive real-time sentiment updates.
- **API Integration**: Integrates Flask API with the React frontend for seamless data handling and visualization.
- **User-Friendly Interface**: The frontend, built with React and TypeScript, includes interactive charts for sentiment trends and educational resources for beginners.

## Tech Stack

### Backend
- **Python**: Data scraping, preprocessing, and Flask API development.
- **BeautifulSoup**: For web scraping news articles.
- **Hugging Face Transformers**: For sentiment analysis with pre-trained NLP models.
- **Flask**: Provides the API layer to serve data to the frontend.

### Frontend
- **React & TypeScript**: For a responsive and dynamic user interface.
- **Chart.js**: For visualizing sentiment trends and stock data.
- **CSS (Tailwind)**: For styling and responsive design.

## Usage
- **Fetch Stock Data**: The system scrapes articles related to predefined stocks from Yahoo Finance and Google News.
- **Run Sentiment Analysis**: News titles are preprocessed and passed through a sentiment analysis model to obtain sentiment scores.
- **Display on Frontend**: Data is displayed on the frontend with sentiment trends and stock insights for the user.
