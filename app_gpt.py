from helper import divide_dataset_by_char_sum, merge_strings, analise_sentimento
import time
import openai
import pandas as pd
import glob
import json


tweets = pd.read_csv('./data/only_clean_tweets.csv')

datasets = divide_dataset_by_char_sum(tweets, 'clean_tweet', 2000)

for i,df in enumerate(datasets):
    # Save the dataset as a CSV file
    df.to_csv(f'datasets_{i}.csv', index=False)
    print(f"Dataset_{i} salvo em datasets_{i}.csv")

#comando = f"Analyze the Elon Musk's tweets regarding the value of Bitcoin. The tweets are separated by '\n' . They can be rated positive, neutral, or negative in sentiment. The answer must be only the sentiment analysis list python style.For the input 'Bitcoin is amazing','The weather is nice','I hate cryptocurrencies'. The result should be ['POSITIVE', 'NEGATIVE', 'NEUTRAL']. The tweets are:"

comando = f"Analyze the Elon Musk's tweets regarding the value of Dogecoin,. tweets are separated by '\n' . They can be rated positive, neutral, or negative in sentiment. The answer must be only the sentiment analysis list python style. For the input 'Dogecoin is amazing','The weather is nice','I hate cryptocurrencies'. The result should be ['POSITIVE', 'NEGATIVE', 'NEUTRAL']. The tweets are:"

j= 0
for i in range(len(datasets)- j):
    res, res_comp = analise_sentimento(merge_strings(datasets[i + j]['clean_tweet'].to_list()), comando, (i + j))
    
    # Sleep to comply with rate limits of the OpenAI API
    time.sleep(1/18 * 80)