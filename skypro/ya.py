from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
for x in range(1,10):
driver.back()
driver.forward()
driver.set_window_size(640, 460) #окно браузера уменьшится под параметры
sleep(50)