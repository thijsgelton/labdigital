from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from products.forms import ProductForm
from products.serializers import ProductSerializer
from .models import Product


def index(request):
    return render(request, "products/index.html")


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def details(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request, "products/details.html", context={"form": form, "product": product})


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, "products/create.html", context={"form": form})


def delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, "products/delete.html", context={"product": product})
