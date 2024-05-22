from selenium.webdriver.common.by import By


class HomePageMesto:
    # локатор кнопки добавления нового места
    add_new_place_button = [By.CLASS_NAME, 'profile__add-button']
    # локатор поля «Название»
    name_field = [By.NAME, 'name']
    # локатор поля «Ссылка на картинку»
    link_to_picture_field = [By.NAME, 'link']
    # локатор кнопки «Сохранить»
    save_button = [By.XPATH, ".//form[@name='new-card']/button[text()='Сохранить']"]

    def __init__(self, driver):
        self.driver = driver

    # метод кликает на кнопку добавления нового места
    def click_add_new_place_button(self):
        self.driver.find_element(*self.add_new_place_button).click()

    # метод вводит название нового места
    def set_name(self):
        new_title = "Новое место"
        self.driver.find_element(*self.name_field).send_keys(new_title)

    # метод вводит ссылку на изображение
    def set_link_to_picture_field(self):
        self.driver.find_element(*self.link_to_picture_field).send_keys("Ссылка на новое изображение")

    # метод кликает на кнопку «Сохранить»
    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    # напиши шаг добавления нового места
