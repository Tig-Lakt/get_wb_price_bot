import os
import sys

import yaml
import logging
from dotenv import load_dotenv

# Добавляем корневой каталог проекта в PYTHONPATH для удобства импорта
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_PATH)

# Загружаем переменные окружения из файла .env
dotenv_path = os.path.join(PROJECT_PATH, ".env")  # Путь к файлу .env
load_dotenv(dotenv_path, override=True)  # Загружает переменные окружения из .env в os.environ

CONFIG_FILE_PATH = os.path.join(PROJECT_PATH, "src", "config.yaml")

logging.basicConfig(level=logging.INFO)


def get_bot_token() -> str:
    """
    Получает токен бота из переменной окружения TELEGRAM_BOT_TOKEN.

    Returns:
        str: Токен бота.
    """
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        logging.error("Ошибка: Переменная окружения TELEGRAM_BOT_TOKEN не задана.")
        return None  # Или raise EnvironmentError

    return token


def update_config_file(token: str=None):
    """
    Обновляет config.yaml с токеном бота.
    """
    config_data = {"bot_token": token}

    try:
        with open(CONFIG_FILE_PATH, "w") as file:
            yaml.dump(config_data, file)
    except Exception as e:
        logging.error(f"Ошибка при записи в config.yaml: {e}")