from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
driver.find_element(By.ID, "email").send_keys("sinegubov_8@gmail.com")

# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, "password").send_keys("123")

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Найди футер
element = driver.find_element(By.TAG_NAME, "footer")

# Прокрути страницу до футера
driver.execute_script("arguments[0].scrollIntoView();", element)

# Проверь, что футер содержит текст 'Mesto Russia'
assert 'Mesto Russia' in element.text

driver.quit()


