from django.test import TestCase
from ..models import MovieFormat, Movie, AboutMovie

class TestMovieFormatModel(TestCase):

    def test_str_method(self):
        movie_format = MovieFormat.objects.create(name="3-D", price=100)
        self.assertEqual(movie_format.__str__(), f"{movie_format.name}:{movie_format.price}")


class TestMovieModel(TestCase):

    def test_str_method(self):
        movie = Movie.objects.create(title="Mad Max 3", age_limit=18, start_date="2022-07-19", end_date="2022-08-19")
        self.assertEqual(movie.__str__(), movie.title)

class TestAboutMovieModel(TestCase):

    def test_str_method(self):
        movie = Movie.objects.create(title="Mad Max 3", age_limit=18, start_date="2022-07-19", end_date="2022-08-19")
        about_movie = AboutMovie.objects.create(movie=movie, title="Mad Max 3")
        self.assertEqual(about_movie.__str__(), about_movie.title)