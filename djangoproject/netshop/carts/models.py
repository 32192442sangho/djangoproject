from django.db import models

from netshop.nusers.models import Nuser
from netshop.products.models import Product


# Create your models here.
class Cart(models.Model):
    use_in_migrations = True
    cart_id = models.AutoField(primary_key=True)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    nuser_id = models.ForeignKey(Nuser, on_delete=models.CASCADE)

    class Meta:
        db_table = "netshop_carts"

    def __str__(self):
        return f"{self.pk} {self.product_id} {self.nuser_id}"