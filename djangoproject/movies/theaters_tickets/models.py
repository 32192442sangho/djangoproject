from django.db import models

from movies.musers.models import Muser
from movies.showtimes.models import Showtime
from movies.theaters.models import Theater


# Create your models here.
class Theater_Ticket(models.Model):
    use_in_migrations = True
    theater_ticket_id = models.AutoField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()

    showtime_id = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    theater_id = models.ForeignKey(Theater, on_delete=models.CASCADE)
    muser_id = models.ForeignKey(Muser, on_delete=models.CASCADE)

    class Meta:
        db_table = "movies_theater_tickets"

    def __str__(self):
        return f"{self.pk} {self.x} {self.y} {self.showtime_id} {self.theater_id} {self.muser_id}"