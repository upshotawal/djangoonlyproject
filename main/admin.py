from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Category
from .models import Item
from .models import Carts
from .models import OrderPlaced
from .models import Customer


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Carts)

admin.site.register(Customer)
admin.site.register(OrderPlaced)
