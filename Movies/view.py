
class MovieView:
    def show_movies(self, movies):
        for movie in movies:
            print(f"Название: {movie.title}")
            print(f"Жанр: {movie.genre}")
            print(f"Режиссер: {movie.director}")
            print(f"Год выпуска: {movie.year}")
            print(f"Длительность: {movie.duration}")
            print(f"Студия: {movie.studio}")
            print(f"Актеры: {', '.join(movie.actors)}")
            print()

    def get_movie_info(self):
        title = input("Введите название фильма: ")
        genre = input("Введите жанр: ")
        director = input("Введите режиссера: ")
        year = input("Введите год выпуска: ")
        duration = input("Введите длительность: ")
        studio = input("Введите студию: ")
        actors = input("Введите имена актеров через запятую: ").split(', ')
        return title, genre, director, year, duration, studio, actors

