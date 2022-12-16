from django.db import models

from netshop.deliveries.models import Delivery
from netshop.nusers.models import Nuser
from netshop.products.models import Product


# Create your models here.
class Order(models.Model):
    use_in_migrations = True
    order_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    nuser_id = models.ForeignKey(Nuser, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    class Meta:
        db_table = "netshop_orders"

    def __str__(self):
        return f"{self.pk} {self.created_at} {self.product_id} {self.nuser_id} {self.delivery_id}"