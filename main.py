import os
from steampy.client import SteamClient
from steampy.models import Currency, GameOptions, PredefinedOptions
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

# Определение игры и настроек
UNTURNED = PredefinedOptions("304930", "2")


# Получение конфиденциальных данных из переменных окружения
API_KEY = config.get("API_KEY")
STEAM_LOGIN = config.get("STEAM_LOGIN")
STEAM_PASSWORD = config.get("STEAM_PASSWORD")    
STEAM_GUARD_FILE = 'steam.json'


if not all([API_KEY, STEAM_LOGIN, STEAM_PASSWORD, STEAM_GUARD_FILE]):
    print("Ошибка: Не все переменные окружения заданы.")
    exit()

# Инициализация SteamClient
steam_client = SteamClient(API_KEY)

try:
    # Попытка войти с логином и файлом
    steam_client.login(STEAM_LOGIN, STEAM_PASSWORD, STEAM_GUARD_FILE)
except Exception as e:
    print(f"Ошибка при входе: {e}")
    exit()

# Проверка ответа от сервера
try:
    response = steam_client.market.fetch_price('Scrubbrush Cobra', game=UNTURNED)
    print(f"Ответ от сервера: {response}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Ошибка при получении цены: {e}")

# Создание ордера на покупку
try:
    response = steam_client.market.create_buy_order("Scrubbrush Cobra", "40", 1, UNTURNED, Currency.UAH)
    buy_order_id = response.get("buy_orderid")
    if buy_order_id:
        print(f"Ордера создан с ID: {buy_order_id}")
    else:
        print("Ошибка: buy_orderid отсутствует в ответе.")
except Exception as e:
    print(f"Ошибка при создании ордера: {e}")