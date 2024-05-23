from faker import Faker

fake = Faker(locale="ru_RU") # создали объект-генератор

def test_user_registration():
    email = fake.email()  # при каждом запуске кода почта будет отличаться
    # дальше тест использует сгенерированный email
    print(email)