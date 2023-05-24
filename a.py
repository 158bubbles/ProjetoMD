import time
import pandas as pd
import glob

df0 = pd.read_csv('dataset_01.csv')
df1 = pd.read_csv('dataset_11.csv')
df2 = pd.read_csv('dataset_21.csv')
df4 = pd.read_csv('dataset_41.csv')
df5 = pd.read_csv('dataset_51.csv')

combined_df = pd.concat([df0, df1, df2, df4, df5], axis=0)

combined_df.to_csv('clean.csv', index=False)
