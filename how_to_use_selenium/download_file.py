from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()
options.add_experimental_option('prefs',{
    "download.default_directory": "C:/repositories/python_selenium/downloads/CHROME.exe",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com/intl/pt-BR/chrome/")   

download_btn = driver.find_element(By.XPATH, "//*[@id='js-download-hero']")
# print(download_btn)
download_btn.click()

sleep(15)

driver.quit()