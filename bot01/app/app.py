#!/home/bot/.virtualenvs/bin/python3

import os
import re
import telebot

from time import sleep
from dotenv import load_dotenv

from utils.parametros import COMANDOS
from utils.parametros import RESPOSTAS
from utils.parametros import boas_vindas
from utils.parametros import informacao
from utils.parametros import saudacao

from utils.registra_interacoes import acessos_bot
from utils.registra_interacoes import execucoes_bot

from utils.memoria_interacoes import registra_ultima_interacao
from utils.memoria_interacoes import verifica_ultima_interacao

from utils.interpretando_interacao import interpretando_interacao


load_dotenv()

TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM", None)

bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(commands=["start"])
def boas_vindas_bot(message):
    acessos_bot(message)
    nome_usuario = message.from_user.first_name
    for mensagem_boas_vindas in boas_vindas(nome_usuario):
        bot.send_message(message.chat.id, mensagem_boas_vindas)
    sleep(3)
    for _, comando in COMANDOS.items():
        bot.send_message(message.chat.id, comando)

@bot.message_handler(commands=["comando1"])
def aulas(message):
    acessos_bot(message)
    for index, resposta in enumerate(RESPOSTAS["comando1"]):
        bot.send_message(message.chat.id, resposta)
        sleep(1) if index == 0 else None

@bot.message_handler(commands=["comando2"])
def agenda(message):
    acessos_bot(message)
    for index, resposta in enumerate(RESPOSTAS["comando2"]):
        bot.send_message(message.chat.id, resposta)
        sleep(1) if index == 0 else None

@bot.message_handler(commands=["comando3"])
def whatsapp(message):
    acessos_bot(message)
    for index, resposta in enumerate(RESPOSTAS["comando3"]):
        bot.send_message(message.chat.id, resposta)
        sleep(1) if index == 0 else None

@bot.message_handler(commands=["comando4"])
def canal(message):
    acessos_bot(message)
    for index, resposta in enumerate(RESPOSTAS["comando4"]):
        bot.send_message(message.chat.id, resposta)
        sleep(1) if index == 0 else None

@bot.message_handler(commands=["comando5"])
def github(message):
    acessos_bot(message)
    for index, resposta in enumerate(RESPOSTAS["comando5"]):
        bot.send_message(message.chat.id, resposta)
        sleep(1) if index == 0 else None

@bot.message_handler(func=lambda message: re.search(r"^[^/]", message.text))
def responde_usuario(message):
    acessos_bot(message)
    interacao = interpretando_interacao(message.text)
    deve_interagir = verifica_ultima_interacao(message.from_user.id, interacao)

    if message.text and "sauda" in interacao and deve_interagir:
        nome_usuario = message.from_user.first_name
        mensagem_usuario = message.text
        bot.reply_to(message, saudacao(nome_usuario, mensagem_usuario))
        registra_ultima_interacao(message.from_user.id, interacao)
    
    elif message.text and "sauda" not in interacao and deve_interagir:
        nome_usuario = message.from_user.first_name
        for id, mensagem_interacao in enumerate(informacao(nome_usuario)):
            bot.reply_to(message, mensagem_interacao) if id == 0 else None
            bot.send_message(message.chat.id, mensagem_interacao) if id > 0 else None
        registra_ultima_interacao(message.from_user.id, interacao)

if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True, timeout=90)
        except Exception as erro:
            execucoes_bot("1000", f"{erro}")
            sleep(30)
            continue
