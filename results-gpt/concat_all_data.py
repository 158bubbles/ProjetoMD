import json
import csv

# List to store the extracted data
data_list = []

for i in range(29):
    dataset_file = f"dataset_{i}.json"
    resultados_file = f"resultado_{i}.json"

    # Load the dataset JSON file
    with open(dataset_file, "r") as dataset_json:
        dataset_data = json.load(dataset_json)

    # Load the resultados JSON file
    with open(resultados_file, "r") as resultados_json:
        resultados_data = json.load(resultados_json)

    # Iterate over the tweets and sentiments
    for tweet_data, sentiment in zip(dataset_data, resultados_data):
        date = tweet_data["date"]
        clean_tweet = tweet_data["clean_tweet"]

        # Append the data to the list
        data_list.append({"date": date, "clean_tweet": clean_tweet, "sentiment": sentiment})

# Define the CSV file path
csv_file = "sentiment_gpt_data.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["date", "clean_tweet", "sentiment"])
    writer.writeheader()
    writer.writerows(data_list)

print(f"CSV file '{csv_file}' has been created successfully.")