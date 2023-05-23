from avaliacoes_tweets import avaliacoes_tweets
from analise_sentimento import analise_sentimento
import time
import openai
import pandas as pd
import glob


"""
for texto in avaliacoes_tweets:
    print(texto)
"""
def merge_strings(strings):
    merged_string = '\n'.join(['"' + s + '"' for s in strings])
    return merged_string


# Find all CSV files starting with "dataset" in the directory
file_pattern = 'dataset*.csv'
csv_files = glob.glob(file_pattern)

# Create an empty list to store the dataframes
dataframes = []

# Load each CSV file into a dataframe
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)
    

# bla = analise_sentimento(merge_strings(dataframes[0]['tweet'].to_list()), 0)

for i, df in enumerate(dataframes):
    res = analise_sentimento(merge_strings(df['clean_tweet'].to_list()), i)
    print(res)
    time.sleep(1/18 * 80)

# for i in range(13):
#     res = analise_sentimento(dataframes[i+22]['tweet'].to_list(), i+22)
#     print(res)
#     time.sleep(1/18 * 80)    
