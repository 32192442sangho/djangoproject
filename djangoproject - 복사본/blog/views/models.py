from django.db import models

from blog.busers.models import Buser
from blog.posts.models import Post


# Create your models here.
class View(models.Model):
    use_in_migrations = True
    view_id = models.AutoField(primary_key=True)
    view_id_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    buser_id = models.ForeignKey(Buser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_views"

    def __str__(self):
        return f"{self.pk} {self.id_address} {self.created_at} {self.buser_id} {self.post_id}"