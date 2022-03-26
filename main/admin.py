from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Category
from .models import Item
from .models import Carts
from .models import OrderPlaced
from .models import Customer
from .models import UserInfo


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Carts)

admin.site.register(Customer)
admin.site.register(OrderPlaced)
admin.site.register(UserInfo)


class Media:
    js = (
        '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
        'js/myscript.js',       # project static folder
    )
