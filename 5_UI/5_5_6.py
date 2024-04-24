from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди элементы
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Проверь атрибут placeholder для каждого элемента
assert email.get_attribute('placeholder') == 'Email'
assert password.get_attribute('placeholder') == "Пароль"

# Закрой браузер
driver.quit()
