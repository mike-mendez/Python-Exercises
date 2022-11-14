from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "../Chrome_Driver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(executable_path=DRIVER_PATH))
url = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url=url)

driver.find_element(By.NAME, "fName").send_keys("Mike")
driver.find_element(By.NAME, "lName").send_keys("Mendez")
driver.find_element(By.NAME, "email").send_keys("mikemendez@mail.com")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
