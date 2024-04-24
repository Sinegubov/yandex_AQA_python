from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://ya.ru")

# Для поиска одного элемента
a = driver.find_element(By.XPATH, ".//img")

# Для поиска группы элементов
b =driver.find_elements(By.XPATH, ".//button")
print(b)
print(a)
driver.quit()