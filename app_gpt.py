from helper import divide_dataset_by_char_sum, merge_strings, analise_sentimento
import time
import openai
import pandas as pd
import glob
import json


tweets = pd.read_csv('./data/only_clean_tweets.csv')

datasets = divide_dataset_by_char_sum(tweets, 'clean_tweet', 2000)


comando = f"Analyze the Elon Musk's tweets regarding the value of Bitcoin,. tweets are separated by '\n' . They can be rated positive, neutral, or negative in sentiment. The answer must be only the sentiment analysis list python style.For the input 'Bitcoin is amazing','The weather is nice','I hate cryptocurrencies'. The result should be ['POSITIVE', 'NEGATIVE', 'NEUTRAL']. The tweets are:"


for i, df in enumerate(datasets):
    res, res_comp = analise_sentimento(merge_strings(df['clean_tweet'].to_list()), comando, i)
    
    try:
        resultado_str = res["resultado"]
        
        if resultado_str.__contains__("Answer"):
            resultado_str = resultado_str.replace("Answer: ", "")
        elif resultado_str.__contains__("Result"):
            resultado_str = resultado_str.replace("Result: ", "")
        else:
            raise KeyError("Neither 'Answer' nor 'Result' found in resultado_str")

        resultado_str = resultado_str.replace("'", "\"")
        resultado_list = json.loads(resultado_str)

        with open(f'resultado_{i}.json', 'w') as file:
            json.dump(resultado_list, file)

        print("Resultado salvo em resultado.json")
    
    except KeyError as e:
        print(f"KeyError: {e}")
        break
    
    time.sleep(1/18 * 80)