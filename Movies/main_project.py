
if __name__ == "__main__":
    from model import Movie
    from controller import MovieController
    from view import MovieView

    controller = MovieController()
    view = MovieView()

    while True:
        print("1. Добавить фильм")
        print("2. Показать все фильмы")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title, genre, director, year, duration, studio, actors = view.get_movie_info()
            movie = Movie(title, genre, director, year, duration, studio, actors)
            controller.add_movie(movie)
        elif choice == "2":
            movies = controller.get_movies()
            view.show_movies(movies)
        elif choice == "3":
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

