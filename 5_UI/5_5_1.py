from selenium import webdriver
import time

# создали драйвер
driver = webdriver.Chrome()

# открыли страницу
driver.get('https://ya.ru/')
assert driver.current_url == 'https://ya.ru/'
assert 'ya.ru' in driver.current_url 
# сделаем паузу
time.sleep(1)

# закроем браузер
driver.quit()
