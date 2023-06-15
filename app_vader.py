from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Initialize the Vader sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load tweets
df = pd.read_csv('only_clean_tweets.csv')

cleaned_tweets = df['clean_tweet'].tolist()

# Perform sentiment analysis on the tweets
sentiment_scores = [sia.polarity_scores(tweet) for tweet in cleaned_tweets]


sentiment_labels = list(map(lambda score: 'POSITIVE' if score['compound'] >= 0.05
                      else 'NEGATIVE' if score['compound'] <= -0.05
                      else 'NEUTRAL', sentiment_scores))

# Print the sentiment and sentiment scores
for tweet, label in zip(cleaned_tweets, sentiment_labels):
    print(f"Tweet: {tweet}\nSentiment: {label}\n")

df['Sentiment'] = sentiment_labels

df.to_csv('label_vader_tweets.csv', index=False)