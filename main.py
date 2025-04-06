from steampy.client import SteamClient
from steampy.models import Currency, GameOptions, PredefinedOptions
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
print(config)

# Определение игры и настроек
UNTURNED = PredefinedOptions("304930", "2")

# Инициализация SteamClient
steam_client = SteamClient('7D808E295C0D481BD801006C94B2004D')

try:
    # Попытка войти с логином и файлом
    steam_client.login('buiidepar', 'm2alonsy1412', 'steam_guard.json')
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

with SteamClient('7D808E295C0D481BD801006C94B2004D', 'buiidepar', 'm2alonsy1412', 'steam_guard.json') as client:
    response = client.market.create_buy_order("Scrubbrush Cobra", "40", 1, UNTURNED, Currency.UAH)
    buy_order_id = response["buy_orderid"]