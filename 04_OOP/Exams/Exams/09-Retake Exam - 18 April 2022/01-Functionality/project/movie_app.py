from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        # self.movies_collection: List[Movie] = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.find_object(self.users_collection, "username", username):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        user = self.find_object(self.users_collection, "username", username)

        if not user:
            raise Exception("This user does not exist!")

        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):
        user = self.find_object(self.users_collection, "username", username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, value in kwargs.items():
            setattr(movie, attr, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie):
        user = self.find_object(self.users_collection, "username", username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):
        user = self.find_object(self.users_collection, "username", username)

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        user = self.find_object(self.users_collection, "username", username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        return "\n".join(m.details() for m in sorted_movies) if sorted_movies else "No movies found."

    def __str__(self):
        users = ", ".join(u.username for u in self.users_collection) if self.users_collection else "No users."
        movies = ", ".join(m.title for m in self.movies_collection) if self.movies_collection else "No movies."

        return (f"All users: {users}\n"
                f"All movies: {movies}")

    # region supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
    # endregion
