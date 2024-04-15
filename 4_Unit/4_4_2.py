class MovieCollection:

    def __init__(self):  # конструктор, который инициализирует пустую коллекцию фильмов
        self.movies = []  # коллекцией будет список: внутри себя словари

    def add_movie(self, name, year, rating):  # Метод добавляет фильм в коллекцию.
        # Создает в списке новый объект с ключами:
        # имя, год, рейтинг

        self.movies.append({"name": name,  # добавляет созданный объект в список фильмов
                            "year": year,
                            "rating": rating})

    def get_movies_by_year(self, year):  # метод получения фильмов из коллекции по определенному году

        def filter_func(obj):  # функция сравнения фильмов по году (нужна для функции фильтрации)
            return obj['year'] == year

        movies_by_year = list(filter(filter_func,
                                     self.movies))  # функция filter перебирает список фильмов, применяя к каждому
        # объекту функцию сравнения
        # в качестве аргументов встроенная в Python функция "filter" принимает функцию сравнения и список, который
        # нужно отфильтровать
        return movies_by_year  # возвращение списка фильмов, которые соответствуют переданному в метод аргументу "year"

    def get_movies_by_more_than_rating(self, rating):  # метод получения фильмов из коллекции выше определенного
        # рейтинга

        def filter_func(object):  # функция сравнения фильмов по рейтингу(нужна для функции фильтрации)
            return object['rating'] >= rating  # рейтинг должен быть выше или равен, чем переданный в аргументе методу

        movies_more_than_rating = list(filter(filter_func, self.movies))

        return movies_more_than_rating  # возвращение списка фильмов, рейтинг которых выше чем переданный в метод
        # аргумент "rating"

    def get_top_of_n_movies(self, n):  # метод получения топ (N) фильмов из коллекции

        def sort_func(movie):  # функция для функции сортировки
            return movie['rating']

        sorted_list = sorted(self.movies, key=sort_func)  # функция сортировки сортирует список по ключу.
        # В качестве ключа передается функция, возвращающая значение, по которому нужно отсортировать список -
        # рейтинг фильмов
        return sorted_list[-n:]  # возвращение из отсортированного по возрастанию списка последние N фильмов


class TestMovieCollection:

    def test_get_movies_by_year_true(self):
        movie_collection = MovieCollection()
        movie_collection.add_movie('The Green Mile', 1999, 9.1)
        movie_collection.add_movie('The Shawshank Redemption', 1994, 9.17)

        movies_by_year = movie_collection.get_movies_by_year(1994)

        assert movies_by_year[0]['year'] == 1994 and len(movies_by_year) == 1

    def test_get_movies_by_more_than_true(self):
        movie_collection = MovieCollection()
        movie_collection.add_movie('The Green Mile', 1999, 9.1)
        movie_collection.add_movie('1+1', 2011, 8.8)
        movies_by_rating = movie_collection.get_movies_by_more_than_rating(9)

        assert movies_by_rating[0]['rating'] > 9

    def test_get_top_of_n_movies_true(self):
        movie_collection = MovieCollection()
        movie_collection.add_movie('The Green Mile', 1999, 9.1)
        movie_collection.add_movie('1+1', 2011, 8.8)
        movie_collection.add_movie('Flight Club', 1999, 8.6)

        top_2_movies_ratings = movie_collection.get_top_of_n_movies(2)
        top_movies_ratings = [movie['rating'] for movie in top_2_movies_ratings]

        assert 8.8 in top_movies_ratings and 9.1 in top_movies_ratings