from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# найди заголовок
print(driver.find_element(By.CSS_SELECTOR, ".auth-form__title")

# Закрой браузер
driver.quit()
