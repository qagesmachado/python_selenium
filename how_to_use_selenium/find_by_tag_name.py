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
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")   

data1 = driver.find_elements(By.TAG_NAME, "h1")[0].text
print(data1)
print("-----")
data2 = driver.find_elements(By.TAG_NAME, "strong")[1].text
print(data2)
print("-----")
data3 = driver.find_elements(By.TAG_NAME, "table")[0].text
print(data3)
print("-----")
data4 = driver.find_elements(By.TAG_NAME, "table")[1].text
print(data4)


driver.quit()