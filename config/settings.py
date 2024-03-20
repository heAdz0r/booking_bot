import os
import configparser

# Чтение конфигурации из файла
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Получение токена бота из конфигурации
BOT_TOKEN = config.get('bot', 'token')