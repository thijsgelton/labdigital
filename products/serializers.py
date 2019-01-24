from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = Product
        fields = ('id', 'title', 'modified_at', 'created_at', 'description', 'price', 'image')
