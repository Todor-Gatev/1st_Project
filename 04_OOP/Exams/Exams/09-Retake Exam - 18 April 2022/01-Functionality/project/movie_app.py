from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    # region supporting methods
    def __get_user_via_username(self, username):
        return next(filter(lambda x: x.username == username, self.users_collection), None)

    @staticmethod
    def __does_user_own_movie(movie, user):
        if not movie.owner == user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    def __is_movie_uploaded(self, movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    # endregion

    def register_user(self, username: str, age: int):
        if self.__get_user_via_username(username):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_user_via_username(username)

        if not user:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.__does_user_own_movie(movie, user)

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        self.__is_movie_uploaded(movie)

        user = self.__get_user_via_username(username)
        self.__does_user_own_movie(movie, user)

        for attr, value in kwargs.items():
            setattr(movie, attr, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        self.__is_movie_uploaded(movie)
        user = self.__get_user_via_username(username)
        self.__does_user_own_movie(movie, user)
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user_via_username(username)

        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        if user.age < movie.age_restriction:
            return

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user_via_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        return "\n".join(m.details() for m in sorted_movies)

    def __str__(self):
        return (f"All users: {', '.join(u.username for u in self.users_collection) or 'No users.'}\n"
                f"All movies: {', '.join(m.title for m in self.movies_collection) or 'No movies.'}")
