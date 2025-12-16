from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.labirint.ru/")
search_field = '#search-field'
driver.find_element(By.CSS_SELECTOR,search_field)
search_input = driver.find_element(By.CSS_SELECTOR,search_field)
sleep(10)
