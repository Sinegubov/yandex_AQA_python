import allure # импорировали библиотеку
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://qa-mesto.praktikum-services.ru/'

@allure.step('Открываем браузер Chrome') # декоратор
def init_driver():
    return webdriver.Chrome()

@allure.step('Открываем страницу {page}') # декоратор
def open_page(driver, page):
    driver.get(page)

@allure.step('Закрываем браузер') # декоратор
def quit_driver(driver):
    driver.quit()

@allure.title('Проверка placeholder у поля email') # декораторы
@allure.description('На странице ищем элемент "email" и проверяем, что его placeholder == "Email"')
@allure.testcase('ссылка на тест-кейс', 'TestCase-112')
@allure.issue('ссылка на баг', 'BUG-113')
def test_check_email_placeholder():
    driver = init_driver()
    open_page(driver, base_url)

    email = driver.find_element(By.ID, "email")
    assert email.get_attribute("placeholder") == 'Email'

    quit_driver(driver)

@allure.title('Проверка placeholder у поля password')
@allure.description('На странице ищем элемент "password" и проверяем, что его placeholder == "Пароль"')
@allure.link(base_url, name='Дополнительная ссылка')
def test_check_password_placeholder():
    driver = init_driver()
    open_page(driver, base_url)

    password = driver.find_element(By.ID, "password")
    assert password.get_attribute("placeholder") == 'Пароль'

    quit_driver(driver)