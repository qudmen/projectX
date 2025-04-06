import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = {f"https://steamcommunity.com/market/listings/304930/Woodland%20Grizzly"}

options = webdriver.ChromeOptions()
options.add_argument(r"C:\Users\Max\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"profile-directory=Default")  # Или другой профиль, например "Profile 1"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# C:\Users\Max\AppData\Local\Google\Chrome\User Data "Max"
# C:\Users\qudme\AppData\Local\Google\Chrome\User Data "Artem"

def buy_item():
    driver.get("https://steamcommunity.com/market/listings/304930/Woodland%20Grizzly")
    time.sleep(5)
    button = driver.find_element("xpath", "//a[contains(@class, 'market_commodity_buy_button') and span[contains(text(), 'Придбати...')]]")
    time.sleep(5)
    button.click()
buy_item()
time.sleep(5)
# driver.quit()