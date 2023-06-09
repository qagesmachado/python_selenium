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

elemento_imagem = driver.find_elements(By.CLASS_NAME, "navbar-brand")[0]
elemento_img = elemento_imagem.find_element(By.TAG_NAME, "img")
atributo_src = elemento_img.get_attribute("src")
print(atributo_src)
print("-----")

elemento = driver.find_element(By.XPATH, "//*[@id='main-nav-nav']//img").get_attribute("alt")
print(elemento)
print("-----")



driver.quit()