from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

DRIVER_PATH = "../Chrome_Driver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(executable_path=DRIVER_PATH))
url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=url)


def play_game(time_sec):
    while time_sec:
        cookie = driver.find_element(By.ID, "cookie")
        stores = driver.find_elements(By.CSS_SELECTOR, "#store > div")
        money = int(driver.find_element(By.ID, "money").text)
        if time_sec & 2 == 0:
            for store in reversed(stores):
                price_str = store.find_element(By.CSS_SELECTOR, "b").text.split(" ")[-1].replace(",", "")
                price_num = int(price_str) if len(price_str) else False
                if money >= price_num and price_num:
                    store.click()
                    break
        cookie.click()

        sleep(1)
        time_sec -= 1

    cookie_per_sec = driver.find_element(By.ID, "cps")
    return cookie_per_sec


print(f"Cookies Per Second: {float(play_game(300).text.split(' ')[-1])}")
