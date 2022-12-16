from django.db import models

from netshop.nusers.models import Nuser


# Create your models here.
class Delivery(models.Model):
    use_in_migrations = True
    delivery_id = models.AutoField(primary_key=True)
    username = models.TextField()
    address = models.TextField()
    detail_address = models.TextField()
    phone = models.TextField()

    nusers_id = models.ForeignKey(Nuser, on_delete=models.CASCADE)

    class Meta:
        db_table = "netshop_deliveries"

    def __str__(self):
        return f"{self.pk} {self.username} {self.address} {self.detail_address} {self.phone} {self.nusers_id}"