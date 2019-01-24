from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductsViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]
