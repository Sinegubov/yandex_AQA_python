from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# найди заголовок
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()
# Закрой браузер
driver.quit()
