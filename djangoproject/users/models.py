from django.db import models

# Create your models here.
class User(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    rank = models.IntegerField()
    point = models.IntegerField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.pk} {self.username} {self.password} {self.created_at} {self.rank} {self.point}"