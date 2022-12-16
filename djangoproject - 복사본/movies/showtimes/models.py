from django.db import models

from movies.cinemas.models import Cinema
from movies.movies.models import Movie
from movies.theaters.models import Theater


# Create your models here.
class Showtime(models.Model):
    use_in_migrations = True
    showtime_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater_id = models.ForeignKey(Theater, on_delete=models.CASCADE)

    class Meta:
        db_table = "movies_showtimes"

    def __str__(self):
        return f"{self.pk} {self.start_time} {self.end_time} {self.cinema_id} {self.movie_id} {self.theater_id}"
