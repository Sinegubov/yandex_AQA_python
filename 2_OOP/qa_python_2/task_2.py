class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies


class Comedy(Movies):

    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Комедии: {self.movies}'


class Drama(Movies):

    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драмы: {self.movies}'


comedies = Comedy()
print(comedies.add_movie('Большой куш'))
dramas = Drama()
print(dramas.add_movie('Оружейный барон'))
