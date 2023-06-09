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
driver.get("https://www.infomoney.com.br/")   

data = driver.find_element(By.ID, "high")
print(data)
print("-----")
data1 = driver.find_element(By.ID, "high").text
print(data1)
print("-----")
data2 = driver.find_elements(By.ID, "high")[0].text
print(data2)

driver.quit()