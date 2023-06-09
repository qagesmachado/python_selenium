from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl

from time import sleep

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")   

wb = openpyxl.Workbook()
ws = wb.active

filmes = driver.find_element(By.XPATH, "//*[@id='main']//table[@data-caller-name='chart-top250movie']")

filme = []

for linha in filmes.find_elements(By.TAG_NAME, "tr"):
    # print(linha.text)
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME, "td"):
        linhaDados.append(coluna.text)
    filme.append(linhaDados)

del filme[0]
filme.insert(0, ('','Rank & Title', 'IMDb Rating',	'Your Rating', '', ''))

for i in filme:
   print(i) 
   ws.append(i)

wb.save('C:/repositories/python_selenium/downloads/output.xlsx')


driver.quit()

