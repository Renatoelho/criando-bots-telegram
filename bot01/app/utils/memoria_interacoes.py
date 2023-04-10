
import redis
from dotenv import load_dotenv

from os import getenv
from datetime import timedelta

from utils.registra_interacoes import execucoes_bot

load_dotenv()

REDIS_HOST = getenv("REDIS_HOST")
REDIS_PORT = int(getenv("REDIS_PORT"))
REDIS_DB = int(getenv("REDIS_DB"))

def verifica_ultima_interacao(user_id: int, interacao: str) -> bool:
    try:
        with redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB) as r:
            if r.exists(f"{user_id}_{interacao}"):
                return False
            else:
                return True
    except Exception as erro:
        execucoes_bot("1002", f"{erro}")
        return True

def registra_ultima_interacao(user_id: int, interacao: str) -> bool:
    try:
        with redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB) as r:            
            tempo_de_vida_horas = 24
            tempo_de_vida = timedelta(hours=tempo_de_vida_horas)
            r.setex(f"{user_id}_{interacao}", tempo_de_vida, "True")
        return True
    except Exception as erro:
        execucoes_bot("1003", f"{erro}")
        return False