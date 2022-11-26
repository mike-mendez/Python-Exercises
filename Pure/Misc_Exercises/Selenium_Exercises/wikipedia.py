from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "../Chrome_Driver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(executable_path=DRIVER_PATH))
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url=url)

num_of_articles = driver.find_element(By.CSS_SELECTOR, "a[title='Special:Statistics']")
print(num_of_articles.text)

wiki_search = driver.find_element(By.NAME, "search")
wiki_search.send_keys("Python")
wiki_search.send_keys(Keys.ENTER)

# num_of_articles.click()
