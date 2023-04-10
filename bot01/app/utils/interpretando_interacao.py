
from os import getenv

import requests
from dotenv import load_dotenv

from utils.registra_interacoes import execucoes_bot
from utils.parametros import MENSAGEM_SAUDACAO


load_dotenv()

TOKEN_CHATGPT3 = getenv("TOKEN_CHATGPT3", None)

def interpretando_interacao(interacao: str) -> str:
    try:
        comando_interacao = (
            "Faça a interpretação no seguinte texto e "
            "retorne uma única palavra classificando em "
            "'saudação' ou 'pergunta' para qualquer "
            f"outra opção: '{interacao}'"
        )
        modelo_engine = "text-davinci-003"
        cabecalho = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN_CHATGPT3}",
        }
        dados = {
            "prompt": comando_interacao,
            "temperature": 0.7,
            "max_tokens": 100,
            "n": 1,
            "stop": None,
        }
        reposta = requests.post(
            f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
            headers=cabecalho,
            json=dados,
        )
        if reposta.status_code != 200:
            assert reposta.raise_for_status()
        resposta = reposta.json()["choices"][0]["text"].strip().lower()
        if "sauda" in resposta:
            return "saudacao"
        else:
            return "pergunta"
    except Exception as erro:
        execucoes_bot("1001", f"{erro}")
        if interacao in MENSAGEM_SAUDACAO:
            return "saudacao"
        else:
            return "pergunta"
