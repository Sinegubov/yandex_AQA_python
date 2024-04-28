from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

list = driver.get_cookies()
print(list)

cookie_name = "_yasc"
cookie = driver.get_cookie(cookie_name)
print(cookie)

new_cookie = {"name": "new_cookie", "value": "new_value"}
driver.add_cookie(new_cookie)
cookie2 = driver.get_cookie(new_cookie)
print(cookie2)

driver.delete_cookie("new_cookie") 

driver.quit()