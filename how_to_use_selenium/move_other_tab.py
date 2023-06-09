from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from time import sleep

# Var
cep_origem = 38410104
cep_destino = 13070752


options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www2.correios.com.br/sistemas/precosPrazos/")   

driver.find_element(By.XPATH, "//input[@name='cepOrigem']").send_keys(cep_origem)
driver.find_element(By.XPATH, "//input[@name='cepDestino']").send_keys(cep_destino)

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

sleep(3)

print(entrega)
print(preco_servico)
print(preco_embalagem)
print(preco_total)
driver.quit()