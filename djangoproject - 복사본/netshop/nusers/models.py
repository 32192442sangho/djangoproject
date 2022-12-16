from django.db import models

# Create your models here.
class Nuser(models.Model):
    use_in_migrations = True
    nuser_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    point = models.IntegerField()

    class Meta:
        db_table = "netshop_nusers"

    def __str__(self):
        return f"{self.pk} {self.email} {self.nickname} {self.password} {self.point}"