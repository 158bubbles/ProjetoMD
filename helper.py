import pandas as pd
import os
import dotenv
import requests
import json

dotenv.load_dotenv()

def divide_dataset_by_char_sum(dataset, column_name, max_chars_threshold):
    
    divided_datasets = []
    current_chars_sum = 382
    current_subset = []
    
    for _, row in dataset.iterrows():
        if (current_chars_sum + len(row[column_name])) <= max_chars_threshold:
        
            current_subset.append(row)
            current_chars_sum += len(row[column_name])
        
        else:
            divided_datasets.append(pd.DataFrame(current_subset))
            current_subset = [row]
            current_chars_sum = 382
            current_chars_sum += len(row[column_name])
    
    return divided_datasets


def merge_strings(strings):
    merged_string = '\n'.join(['"' + s + '"' for s in strings])
    return merged_string


def analise_sentimento(texto: str, prompt: str, i: int) -> str:
    CHAVE_API = os.getenv("CHAVE_API", None)
    modelo_engine = "text-davinci-003"
    comando = prompt + texto

    cabecalho = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_API}"
    }

    dados = {
        "prompt": comando,
        "temperature": 0,
        "max_tokens": 2047,
        "n": 1,
        "stop": None,
    }

    resposta = requests.post(
        f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
        headers=cabecalho,
        json=dados
    )
    

    resposta_json = resposta.json()
    #print(resposta_json)
    resultado = resposta_json['choices'][0]['text'].strip()

    data = {
        'resultado': resultado,
    }

    with open(f'resultado_{i}.json', 'w') as file:
        json.dump(data, file)

    print("Resultado salvo em resultado.json")
    return data
