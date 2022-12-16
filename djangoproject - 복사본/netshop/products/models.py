from django.db import models

from netshop.categories.models import Category


# Create your models here.
class Product(models.Model):
    use_in_migrations = True
    product_id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    image_url = models.TextField()

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "netshop_products"

    def __str__(self):
        return f"{self.pk} {self.name} {self.price} {self.image_url} {self.category_id}"