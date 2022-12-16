from django.db import models

from movies.cinemas.models import Cinema


# Create your models here.
class Theater(models.Model):
    use_in_migrations = True
    theater_id = models.AutoField(primary_key=True)
    title = models.TextField()
    seat = models.TextField()

    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    class Meta:
        db_table = "movies_theaters"

    def __str__(self):
        return f"{self.pk} {self.title} {self.seat} {self.cinema_id}"