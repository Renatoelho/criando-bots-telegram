
-- Modelagem Bot Telegram

# Interações de acessos com o Bot Telegram

CREATE TABLE IF NOT EXISTS 
db_bots_telegram.interacoes_acessos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  origin VARCHAR(50),
  message_id BIGINT(19),
  user_id BIGINT(19),
  username VARCHAR(50),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  is_bot VARCHAR(20),
  language_code VARCHAR(20),
  type VARCHAR(50),
  is_premium VARCHAR(20),
  date_time DATETIME,
  text TEXT
);


INSERT INTO db_bots_telegram.interacoes_acessos
(origin, message_id, user_id, username, first_name, 
last_name, is_bot, language_code, type, is_premium, 
date_time, text)
VALUES (
'${valor_origin}',
${valor_message_id},
${valor_user_id}, 
'${valor_username}', 
'${valor_first_name}', 
'${valor_last_name}', 
'${valor_is_bot}', 
'${valor_language_code}', 
'${valor_type}', 
'${valor_is_premium}', 
'${valor_date_time}', 
'${valor_text}'
);

SELECT * FROM db_bots_telegram.interacoes_acessos ia;


# Interações de execuções do Bot Telegram (erros de execução da aplicação)

CREATE TABLE IF NOT EXISTS db_bots_telegram.interacoes_acessos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  origin VARCHAR(50),
  message_id BIGINT(19),
  user_id BIGINT(19),
  username VARCHAR(50),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  is_bot VARCHAR(20),
  language_code VARCHAR(20),
  type VARCHAR(50),
  is_premium VARCHAR(20),
  date_time DATETIME,
  text TEXT
);


INSERT INTO db_bots_telegram.interacoes_acessos
(origin, message_id, user_id, username, first_name, 
last_name, is_bot, language_code, type, is_premium, 
date_time, text)
VALUES (
'${valor_origin}',
${valor_message_id},
${valor_user_id}, 
'${valor_username}', 
'${valor_first_name}', 
'${valor_last_name}', 
'${valor_is_bot}', 
'${valor_language_code}', 
'${valor_type}', 
'${valor_is_premium}', 
'${valor_date_time}', 
'${valor_text}'
);

SELECT * FROM db_bots_telegram.interacoes_execucoes ie;

