
from os import getenv
from dotenv import load_dotenv

load_dotenv()

COMANDOS = (
    {
    "comando1": "/comando1 - Add conteúdo aqui...",
    "comando2": "/comando2 - Add conteúdo aqui...",
    "comando3": "/comando3 - Add conteúdo aqui...",
    "comando4": "/comando4 - Add conteúdo aqui...",
    "comando5": "/comando5 - Add conteúdo aqui...",

    }
)

RESPOSTAS = (
    {
    "comando1": (
        [
            "Ação 1:",
            "https://..."
        ]
    ),
    "comando2": (
        [
            "Ação 2:",
            "https://..."
        ]
    ),
    "comando3": (
        [
            "Ação 3:",
            "https://..."
        ]
    ),
    "comando4": (
        [
            "Ação 4:",
            "https://..."
        ]
    ),
    "comando5": (
        [
            "Ação 5:",
            "https://..."
        ]
    )
    }
)

MENSAGEM_SAUDACAO = (
    [
        "Olá!",
        "Bom dia",
        "Oi tudo bem?",
        "Boa tarde!",
        "Boa noite!"
    ]
)

def boas_vindas(nome: str) -> list:
    texto1 = (
        f"Olá, {nome}. Eu sou o <Nome do seu Assistente> \U0001F916, "
        "assistente virtual do <Seu Nome>."
    )
    texto2 = "Escolha e clique em uma das opções abaixo:"
    return [texto1, texto2]

def informacao(nome: str) -> list:
    texto1 = (
        f"Ok, {nome}. Converse diretamente com o "
        "<Seu Nome> no Telegram. Como "
        "sou um robô \U0001F916 e novato aqui, posso me "
        "confundir com a grande quantidade de mensagens."
    )
    texto2 = "Esse é o contato direto do <Seu Nome>:"
    texto3 = f"{getenv('URL_TELEGRAM')}"
    return [texto1, texto2, texto3]

def saudacao(nome: str, mensagem: str) -> str:
    texto = (
        f"{mensagem}, {nome}. Em que posso ajudar?"
    )
    return texto
