from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Category
from .models import Item


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Item)
