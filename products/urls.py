from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductsViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('details/<int:pk>', views.details, name='details'),
    path('delete/<int:pk>', views.delete, name='delete')
]
