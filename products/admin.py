from django.contrib import admin
from .models import Product
from reversion.admin import VersionAdmin


class BaseReversionAdmin(VersionAdmin):
    pass


# Register your models here.
admin.site.register(Product, BaseReversionAdmin)
