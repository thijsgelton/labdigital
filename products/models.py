from datetime import datetime
from versatileimagefield.fields import VersatileImageField
from django.db import models
from django.dispatch import receiver

# Create your models here.
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


class Product(models.Model):
    created_at = models.DateTimeField(default=datetime.now(), verbose_name="Created at")
    modified_at = models.DateTimeField(default=datetime.now(), verbose_name="Modified at")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = VersatileImageField(upload_to="products")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


@receiver(models.signals.post_save, sender=Product)
def warm_product_image(sender, instance, **kwargs):
    """
    Create all sizes on save
    """
    product_image_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set=[
            ('large_horiz_crop', '1200x600'),
            ('large_vert_crop', '600x1200'),
        ],
        image_attr='image'
    )
