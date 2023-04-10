
from json import dump
from pathlib import Path
from os.path import abspath
from datetime import datetime
from uuid import uuid5
from uuid import NAMESPACE_OID


caminho_interacoes = f"{Path(abspath(__file__)).parent.parent}/interacoes"


def _cria_diretorio(caminho: str) -> bool:
    try:
        Path(caminho).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as _:
        _ = _
        return False


def _registra_interacoes(interacao: str) -> bool:
    try:
        code_uuid5 = (
            uuid5(
                NAMESPACE_OID,
                str(datetime.now().strftime('%Y%m%d%H%M%S%s'))
            )
        )
        nome_arquivo = f"interacao-bot-{code_uuid5}.json"
        _cria_diretorio(caminho_interacoes)
        with open(f"{caminho_interacoes}/{nome_arquivo}", "w") as arquivo:
            dump(interacao, arquivo)
        return True
    except Exception as _:
        _ = _
        return False


def acessos_bot(message: object) -> bool:
    try:
        converte_timestamp = (
            datetime
            .fromtimestamp(message.date)
            .strftime('%Y-%m-%d %H:%M:%S')
        )
        registro_interacoes = (
            {
                "origin": "ACESSOS",
                "message_id": message.message_id,
                "user_id": message.from_user.id,
                "username": message.from_user.username,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
                "is_bot": message.from_user.is_bot,
                "language_code": message.from_user.language_code,
                "type": message.chat.type,
                "is_premium": message.from_user.is_premium,
                "date_time": converte_timestamp,
                "text": message.text
            }
        )
        _registra_interacoes(registro_interacoes)
        return True
    except Exception as _:
        _ = _
        return False


def execucoes_bot(code_erro: str, message_erro: str) -> bool:
    try:
        registro_interacoes = (
            {
                "origin": "EXECUCAO",
                "code_erro": code_erro,
                "date_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "message_erro": message_erro
            }
        )
        _registra_interacoes(registro_interacoes)
        return True
    except Exception as _:
        _ = _
        return False
