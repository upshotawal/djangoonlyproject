from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
STATUS = (
    (0, "UnAvilable"),
    (1, "Avilable")
)


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse("api:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='00')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    InvoiceNo = models.CharField(_("InvoiceNo"), max_length=135, default=00000)
    StockCode = models.CharField(_("StockCode"), max_length=135, default=00000)
    Description = models.CharField(_("Description"), max_length=255, null=True)
    Quantity = models.IntegerField(_("Quantity"), default=000)
    InvoiceDate = models.DateTimeField(
        _("InvoiceDate"), auto_now=True, null=True)
    UnitPrice = models.FloatField(_("UnitPrice"), max_length=255)
    CostumerId = models.IntegerField(_("CostumerId"))
    Country = models.CharField(_("Country"), max_length=255)
