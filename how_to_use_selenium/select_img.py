from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

from time import sleep

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.imdb.com/")   

driver.maximize_window()

input = driver.find_elements(By.NAME, "q")[0]
input.send_keys("Titanic")
input.send_keys(Keys.ENTER)

titanic_title = driver.find_element(By.XPATH,"//section[@data-testid='find-results-section-title']//a[text()[contains(.,'Titanic')]]").click()
sleep(3)
all_img = driver.find_element(By.XPATH,"//*[@id='__next']//div//span[text()[contains(.,'Elenco principal')]]/../../../../..//div[@data-testid='shoveler-items-container']")
leo = all_img.find_element(By.XPATH, "//img[@alt='Leonardo DiCaprio']")
image_leo = leo.get_attribute("src")
print(image_leo)

try:
    urllib.request.urlretrieve(image_leo, r"C:\repositories\python_selenium\downloads\teste.jpg")
    print('baixado')
except:
    print('Deu ruim')

driver.quit()

