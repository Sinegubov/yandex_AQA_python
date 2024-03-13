class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        return self.movies.append(movie)


class Comedy(Movies):

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'


class Drama(Movies):

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'


comedies = Comedy()
print(comedies.add_movie('Большой куш'))
dramas = Drama()
print(dramas.add_movie('Оружейный барон'))
