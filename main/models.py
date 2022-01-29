from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "UnAvilable"),
    (1, "Avilable")
)   

    
class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.CharField(max_length=256, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    # def get_absolute_url(self):
    #     return reverse("api:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name
    
        
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
      verbose_name_plural = 'Products'
      ordering = ('-created',) 
      
    def __str__(self):
        return self.title