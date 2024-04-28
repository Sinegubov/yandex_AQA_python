from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# напиши код для добавления куки
driver.add_cookie({"name": "my_first_cookie", "value": "15"})

# Проверь поле value для добавленной куки
cookie = driver.get_cookie("my_first_cookie")
assert cookie['value'] == '15'

driver.quit()
