from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = "../Chrome_Driver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
url = "https://www.python.org/"
driver.get(url=url)
events = driver.find_elements(By.CSS_SELECTOR, "div.event-widget > div > ul > li")  # CSS SELECTOR

upcoming_events = {}
for event in events:
    upcoming_events.update({
        events.index(event): {
            "time": event.find_element(By.TAG_NAME, "time").text,
            "name": event.find_element(By.TAG_NAME, "a").text
        }
    })

print(upcoming_events)

driver.quit()
