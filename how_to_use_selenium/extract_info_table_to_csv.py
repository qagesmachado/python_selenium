from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import sleep

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.w3schools.com/html/html_tables.asp")   
driver.maximize_window()

tabela = driver.find_element(By.ID, "customers")
# print(tabela)
dados = []

for linha in tabela.find_elements(By.TAG_NAME, "tr"):
    print(linha.text)
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME, "td"):
        linhaDados.append(coluna.text)
    dados.append(linhaDados)

print(dados)
df = pd.DataFrame(dados)
df = df.iloc[1:, :]
df.columns= ['Company','Contact', 'Country']
print(df)

df.to_csv("C:/repositories/python_selenium/downloads/dados.csv")




driver.quit()

