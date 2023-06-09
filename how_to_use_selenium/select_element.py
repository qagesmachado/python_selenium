from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.amazon.com.br/")  

driver.maximize_window()

text_insert = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
sleep(1)
text_insert.send_keys("Livro")
sleep(1)
text_insert.send_keys(Keys.ENTER)

sleep(3)

# Selecionando por value
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_value("relevanceblender")
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_value("price-asc-rank")
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_value("price-desc-rank")
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_value("review-rank")
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_value("date-desc-rank")
sleep(3)

# Selecionando por index
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_index(0)
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_index(1)
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_index(2)
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_index(3)
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_index(4)
sleep(3)

# Selecionando por text
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_visible_text("Em destaque")
sleep(3)
btn_sort = Select(driver.find_element(By.ID, "s-result-sort-select")).select_by_visible_text("Preço: Do menor para o maior")
sleep(3)

driver.quit()