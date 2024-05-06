from selenium import webdriver
from selenium.webdriver.common.by import By

def test_email_and_password_value():
    # создали драйвер для браузера Chrome
    driver = webdriver.Chrome()
    # перешли на сайт с указанным url
    driver.get('https://qa-mesto.praktikum-services.ru/')

    # ввели Email
    driver.find_element(By.ID, 'email').send_keys('Email')
    # ввели пароль
    driver.find_element(By.ID, 'password').send_keys('Пароль')

    # проверили соответствие поля «Email» переданным данным
    actually_value = driver.find_element(By.ID, 'email').get_property("value")
    expected_value = 'Email'
    assert actually_value == expected_value, f'Ожидалось значение поля Email: "{expected_value}", получено "{actually_value}"'

    # проверили соответствие поля «Пароль» переданным данным
    actually_value = driver.find_element(By.ID, 'password').get_property("value")
    expected_value = 'Пароль'
    assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'