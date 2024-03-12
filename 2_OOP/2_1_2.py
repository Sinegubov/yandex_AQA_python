class Book:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self, page):
        return f"Читаем книгу '{self.title}' - {self.content[page]}"


class Audiobook(Book):

    def __init__(self, title, content):
        self.title = title
        self.content = content
        super().__init__(title, content)

    def listen(self, page):
        return f"Воспроизводим страницу {self.content[page]} из аудиокниги '{self.title}'"


book = Book("Война и мир", ["Страница 1", "Страница 2", "Страница 3"])
print(book.read(1))          # Читаем книгу Война и мир - Страница 2

audiobook = Audiobook("1984", ["Страница 1", "Страница 2"])
print(audiobook.listen(1))   # Воспроизводим страницу 1 из аудиокниги 1984
