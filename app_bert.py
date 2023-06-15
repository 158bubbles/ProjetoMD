
import pandas as pd
import requests
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


df = pd.read_csv('./data/only_clean_tweets.csv')

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("svalabs/twitter-xlm-roberta-bitcoin-sentiment")
# model = AutoModelForSequenceClassification.from_pretrained("svalabs/twitter-xlm-roberta-bitcoin-sentiment")

# tokenizer = AutoTokenizer.from_pretrained("laurens88/finetuning-crypto-tweet-sentiment-test2")
# model = AutoModelForSequenceClassification.from_pretrained("laurens88/finetuning-crypto-tweet-sentiment-test2")

tokenizer = AutoTokenizer.from_pretrained("zainalq7/autotrain-NLU_crypto_sentiment_analysis-754123133")
model = AutoModelForSequenceClassification.from_pretrained("zainalq7/autotrain-NLU_crypto_sentiment_analysis-754123133")

# Modify the model configuration for 3 labels
model.config.num_labels = 3

# Move the model to the GPU device
model.to(device)
cleaned_tweets = df['clean_tweet'].tolist()

# Preprocess and tokenize the tweets
tokenized_inputs = tokenizer(cleaned_tweets, padding=True, truncation=True, return_tensors="pt")

# Move the tokenized inputs to the GPU device
tokenized_inputs = {k: v.to(device) for k, v in tokenized_inputs.items()}

# Pass the tokenized inputs through the model
outputs = model(**tokenized_inputs)

# Get the predicted sentiment labels (positive, neutral, or negative)
predicted_labels = torch.argmax(outputs.logits, dim=1)
print(predicted_labels)

# Define label mapping
label_map = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}

# Map the predicted_labels
predicted_labels = [label_map[label.item()] for label in predicted_labels]

# Print the predicted labels for each tweet
for tweet, label in zip(cleaned_tweets, predicted_labels):
    print(f"Tweet: {tweet}\nSentiment: {label}\n")

df['Sentiment'] = predicted_labels

df.to_csv('./data/label_bert_zainalq7_tweets.csv', index=False)