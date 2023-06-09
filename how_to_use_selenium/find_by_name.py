from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.imdb.com/")   

input = driver.find_elements(By.NAME, "q")[0]
input.send_keys("Titanic" + Keys.ENTER)
# input.send_keys(Keys.ENTER)



driver.quit()