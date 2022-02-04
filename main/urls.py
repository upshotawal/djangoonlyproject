from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path("", views.index, name="index"),
    path("products/", views.product, name="product"),
    path('products/<slug:slug>/', views.product_details, name='product_detail'),
]
