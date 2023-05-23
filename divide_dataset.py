import pandas as pd

test = pd.read_csv('test.csv')

def divide_dataset_by_char_sum(dataset, column_name, max_chars_threshold):
    dataset_sorted = dataset.sort_values(by=column_name, key=lambda x: x.str.len(), ascending=False)
    max_chars = dataset_sorted[column_name].str.len().max()
    
    divided_datasets = []
    current_chars_sum = 30
    current_subset = []
    
    for _, row in dataset_sorted.iterrows():
        current_subset.append(row)
        current_chars_sum += len(row[column_name])
        
        if current_chars_sum >= max_chars_threshold:
            divided_datasets.append(pd.DataFrame(current_subset))
            current_subset = []
            current_chars_sum = 30
    
    if current_subset:
        divided_datasets.append(pd.DataFrame(current_subset))
    
    return divided_datasets

# 2000 *4 que é o limite de tokens a enviar, pois ainda falta somar os do prompt
datasets = divide_dataset_by_char_sum(test, 'tweet', 8000)

# Save the datasets into multiple CSV files with different names
for i, dataset in enumerate(datasets):
    dataset.to_csv(f'data\dataset_{i}.csv', index=False)
