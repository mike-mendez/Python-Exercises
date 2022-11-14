from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = "../Chrome_Driver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
url = "https://www.amazon.com/Bowers-Wilkins-Over-Ear-Headphones-Model/dp/B0B34FFGPT/ref=sr_1_5?crid=BEAWCPQPXW7P&keywords=bowers+%26+wilkins+px8&qid=1668388833&sprefix=bowers+%26+wilkins+px%2Caps%2C268&sr=8-5"
driver.get(url=url)

price = driver.find_element(By.CSS_SELECTOR, "span.a-offscreen+span")
print(price.text)
