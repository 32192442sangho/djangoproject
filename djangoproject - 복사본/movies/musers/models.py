from django.db import models

# Create your models here.
class Muser(models.Model):
    use_in_migrations = True
    muser_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    age = models.IntegerField()

    class Meta:
        db_table = "movies_musers"

    def __str__(self):
        return f"{self.pk} {self.email} {self.nickname} {self.password} {self.age}"