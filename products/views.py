from django.shortcuts import render
from rest_framework import viewsets

from products.serializers import ProductSerializer
from .models import Product


def index(request):
    return render(request, "products/index.html")


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
