import pandas as pd

test = pd.read_csv('filtered_tweets.csv')


def divide_dataset_by_char_sum(dataset, column_name, max_chars_threshold):
    
        
    divided_datasets = []
    current_chars_sum = 210
    current_subset = []
    
    for _, row in dataset.iterrows():
        if (current_chars_sum + len(row[column_name])) <= max_chars_threshold:
        
            current_subset.append(row)
            current_chars_sum += len(row[column_name])
        
        else:
            divided_datasets.append(pd.DataFrame(current_subset))
            current_subset = [row]
            current_chars_sum = 210
            current_chars_sum += len(row[column_name])
    
    return divided_datasets

# 2000 *4 que é o limite de tokens a enviar, pois ainda falta somar os do prompt
datasets = divide_dataset_by_char_sum(test, 'clean_tweet', 3000)

# Save the datasets into multiple CSV files with different names
for i, dataset in enumerate(datasets):
    dataset.to_csv(f'dataset_{i}.csv', index=False)
