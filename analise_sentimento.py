import os
import dotenv
import requests
import json

dotenv.load_dotenv()

def analise_sentimento(texto: str, i: int) -> str:
    CHAVE_API = os.getenv("CHAVE_API", None)
    modelo_engine = "text-davinci-003"
    #comando = f"Responda em uma única palavra, sendo positivo, neutro ou negativo o sentido contido no seguinte texto, sabendo que foi o Elon Musk que escreveu: '{texto}'"
    #comando = f"Identify Elon Musk's tweets regarding the value of Bitcoin, separated by \n as positive, neutral, or negative sentiment. Make the answer simple Python list. Answer only the list of sentiments, not the tweets.  \n'{texto}'"
    comando = f"Analyze the following Elon Musk's tweets and determine if the sentiment regarding the value of Bitcoin is: POSITIVE, NEGATIVE or NEUTRAL. Answer just a POSITIVE, NEGATIVE or NEUTRAL sentiment for each tweet: '{texto}'"

    # comando = f"Analyze the following Elon Musk's tweets and determine if the sentiment reggarding bitcoin is: positive, negative or neutral. Return only a single word, either POSITIVE, NEGATIVE or NEUTRAL in a list: {texto}"
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
    resultado = resposta_json['choices'][0]['text'].strip()

    data = {
        'resultado': resultado,
    }

    with open(f'resultado_{i}.json', 'w') as file:
        json.dump(data, file)

    print("Resultado salvo em resultado.json")
    return resposta_json