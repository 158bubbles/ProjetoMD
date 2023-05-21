import os
import dotenv
import requests
import json

dotenv.load_dotenv()

def analise_sentimento(texto: str) -> str:
    CHAVE_API = os.getenv("CHAVE_API", None)
    modelo_engine = "text-davinci-003"
    #comando = f"Responda em uma única palavra, sendo positivo, neutro ou negativo o sentido contido no seguinte texto, sabendo que foi o Elon Musk que escreveu: '{texto}'"
    comando = f"Based on Elon Musk's tweets about the value of Bitcoin, could you classify each tweet as positive, neutral, or negative sentiment: '{texto}'"

    cabecalho = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_API}"
    }

    dados = {
        "prompt": comando,
        "temperature": 0.7,
        "max_tokens": 35,
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

    with open('resultado.json', 'w') as file:
        json.dump(data, file)

    print("Resultado salvo em resultado.json")
    return resultado