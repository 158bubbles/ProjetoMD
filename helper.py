import pandas as pd
import os
import dotenv
import requests
import json

dotenv.load_dotenv()

def divide_dataset_by_char_sum(dataset, column_name, max_chars_threshold):
    # Initialize variables
    divided_datasets = []  
    current_chars_sum = 382  
    current_subset = [] 
    
    # Iterate over each row in the dataset
    for _, row in dataset.iterrows():
        if (current_chars_sum + len(row[column_name])) <= max_chars_threshold:
            
            current_subset.append(row) 
            current_chars_sum += len(row[column_name]) 
            
        else:

            divided_datasets.append(pd.DataFrame(current_subset))
            
            current_subset = [row]

            current_chars_sum = 382
            current_chars_sum += len(row[column_name])
    
    # Append the final current subset to the divided_datasets list as a DataFrame
    if current_subset:
        divided_datasets.append(pd.DataFrame(current_subset))
    
    # Return the list of divided datasets
    return divided_datasets



def merge_strings(strings):
    merged_string = '\n'.join(['"' + s + '"' for s in strings])
    return merged_string


def analise_sentimento(texto: str, prompt: str, i: int) -> str:
    # Get the API key from the environment variable
    CHAVE_API = os.getenv("CHAVE_API", None)
    
    # Set the model engine
    modelo_engine = "text-davinci-003"
    
    # Construct the command by combining the prompt and the input text
    comando = prompt + texto

    # Set the headers for the API request
    cabecalho = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_API}"
    }

    # Set the data payload for the API request
    dados = {
        "prompt": comando,
        "temperature": 0,
        "max_tokens": 2047,
        "n": 1,
        "stop": None,
    }

    # Send a POST request to the OpenAI API to get the completion
    resposta = requests.post(
        f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
        headers=cabecalho,
        json=dados
    )
    
    # Extract the JSON response
    resposta_json = resposta.json()

    # Get the resulting text from the API response
    resultado = resposta_json['choices'][0]['text'].strip()

    resultado = resultado.replace('\n', '')

    # Find the start and end index of the sentiment list
    start_index = resultado.find("[")
    end_index = resultado.find("]") + 1

    # Extract the context
    context = resultado[start_index:end_index].strip("[]").split("', '")
    # Remove the single quotes from all elements
    context = [element.replace("'", "") for element in context]

    # Prepare the data to be saved in a JSON file
    data = {
        'resultado': context,
    }

    

    # Save the data to a JSON file
    with open(f'resultado_{i}.json', 'w') as file:
        json.dump(data, file)

    # Print a message indicating the result has been saved
    print("Resultado salvo em resultado.json")
    print(resposta_json)
    # Return the data and the JSON response
    return data, resposta_json