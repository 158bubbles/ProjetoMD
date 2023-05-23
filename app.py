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

# Find all CSV files starting with "dataset" in the directory
file_pattern = 'data\dataset*.csv'
csv_files = glob.glob(file_pattern)

# Create an empty list to store the dataframes
dataframes = []

# Load each CSV file into a dataframe
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

analise_sentimento(dataframes[0]['tweet'].to_list(), 0)

# for i, df in enumerate(dataframes):
#     analise_sentimento(df['tweet'].to_list(), i)
#     time.sleep(1/18 * 80)
