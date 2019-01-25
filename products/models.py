from django.db import models
from versatileimagefield.fields import VersatileImageField


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified at")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = VersatileImageField(upload_to="products")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
