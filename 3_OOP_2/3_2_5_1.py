class EBook:
    def __init__(self, content):
        self.__content = content
        self.__current_page = 0

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, new_content):
        self.__content = new_content
    # ... создай сеттер для свойства content

    @property
    def current_page(self):
        return self.__current_page

    # ... создай сеттер для свойства current_page
    @current_page.setter
    def current_page(self, page_number):
        if page_number < 0:
            self.__current_page = 0
        elif page_number >= len(self.__content):
            self.__current_page = len(self.__content) - 1
        else:
            self.__current_page = page_number
