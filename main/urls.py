from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path("", views.index, name="index"),
    path("checkout/", views.checkout, name="checkout"),
    # path("cart/", views.cart, name="cart"),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.show_cart, name="show_cart"),

    path("products/", views.product, name="product"),
    path("items/", views.item, name="item"),

    path('products/<slug:slug>/', views.product_details, name='product_detail'),
    path("update_item/", views.updateItem, name="update_item"),
    path('api/verify_payment', views.verify_payment, name='verify_payment'),
]
