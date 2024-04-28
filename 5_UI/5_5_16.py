from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID, "email").send_keys("sinegubov_8@gmail.com")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Добавь явное ожидание для загрузки списка карточек контента
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "places__list")))

# Найди карточку контента и сделай скролл до неё
element = driver.find_element(By.CSS_SELECTOR, ".places__item")

# Прокрути страницу до футера
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.quit()