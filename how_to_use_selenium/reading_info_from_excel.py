from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import xlsxwriter
import pandas as pd
from time import sleep

# Var
cep_origem = 38410104
cep_destino = 13070752
df = pd.read_excel("C:/repositories/python_selenium/how_to_use_selenium/correio.xlsx")
valor_total = []
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www2.correios.com.br/sistemas/precosPrazos/")  

for index, row in df.iterrows():
    driver.find_element(By.XPATH, "//input[@name='cepOrigem']").send_keys(str(row['origem']))
    driver.find_element(By.XPATH, "//input[@name='cepDestino']").send_keys(str(row['destino']))

    driver.find_element(By.XPATH, "//select[@name='servico']").click()
    Select(driver.find_element(By.XPATH, "//select[@name='servico']")).select_by_index(15)

    driver.find_element(By.XPATH, "//*[@id='spanTipoEmbalagem']//button[text()[contains(.,'Selecionar esta')]][1]").click()

    Select(driver.find_element(By.XPATH, "//*[@id='spanServicoSelecionado']//select[@name='peso']")).select_by_index(2)

    driver.find_element(By.XPATH, "*//input[@value='Calcular']").click()

    driver.switch_to.window(driver.window_handles[1])

    ## Geting values from page

    entrega = driver.find_element(By.XPATH, "//table[@class='comparaResult']//th[text()[contains(.,'Entrega:')]]/../td").text
    preco_servico = driver.find_element(By.XPATH, "//table[@class='comparaResult']//th[text()[contains(.,'Preço do serviço:')]]/../td").text
    preco_embalagem = driver.find_element(By.XPATH, "//table[@class='comparaResult']//th[text()[contains(.,'Embalagem dos Correios')]]/../td").text
    preco_total = driver.find_element(By.XPATH, "//table[@class='comparaResult']//tr[@class='destaque']/th[text()[contains(.,'Valor total:')]]/../td").text

    print(entrega)
    print(preco_servico)
    print(preco_embalagem)
    print(preco_total)

    ## Adding lista
    valor_total.append(preco_total)

    # back
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()

# Adding excel
data = {'origem': df.iloc[:,0], 'destino': df.iloc[:,1], 'valor_total':valor_total}
df2 = pd.DataFrame(data)

df2.to_excel('C:/repositories/python_selenium/downloads/output.xlsx', engine='xlsxwriter')
print(df2)

driver.quit()
