#from avaliacoes_tweets import avaliacoes_tweets
#from analise_sentimento import analise_sentimento
from helper import divide_dataset_by_char_sum, merge_strings, analise_sentimento
import time
import openai
import pandas as pd
import glob
import json


tweets = pd.read_csv('only_clean_tweets.csv')

datasets = divide_dataset_by_char_sum(tweets, 'clean_tweet', 2000)

#datasets[0].to_csv("A.csv")


comando = f"Analyze the Elon Musk's tweets regarding the value of Bitcoin,. tweets are separated by '\n' . They can be rated positive, neutral, or negative in sentiment. The answer must be only the sentiment analysis list python style.For the input 'Bitcoin is amazing','The weather is nice','I hate cryptocurrencies'. The result should be ['POSITIVE', 'NEGATIVE', 'NEUTRAL']. The tweets are:"


for i, df in enumerate(datasets):
    
    res = analise_sentimento(merge_strings(datasets[0]['clean_tweet'].to_list()), comando, i)
        
    resultado_str = res["resultado"]
    resultado_str = resultado_str.replace("Answer: ", "").replace("'", "\"")
    resultado_list = json.loads(resultado_str)

    time.sleep(1/18 * 80)