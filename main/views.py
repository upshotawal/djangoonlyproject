import requests
import json
from decimal import *
from pickle import GET
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models import Q
import joblib


# Create your views here.

def result(request):
    cls1 = joblib.load('ml_recommendor_model.joblib')
    #cls2 = joblib.load('ml_recommendor.joblib')

    ans = cls1.show_recommendations("cream")
    return request(request, "result.html", {'ans': ans})


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        products = Products.objects.filter(title__icontains=q)
    else:
        products = Products.objects.all()[1:4]
    return render(request, "main/home.html", {"products": products})


@login_required(login_url='login')
def product(request):
    if 'q' in request.GET:
        q = request.GET['q']
        products = Products.objects.filter(title__icontains=q)
    else:

        products = Products.objects.all()
    return render(request, "main/product.html", {"products": products})


@login_required(login_url='login')
def item(request):
    items = Item.objects.all()[1:100]
    return render(request, "main/item.html", {"items": items})


@login_required(login_url='login')
def product_details(request, slug):
    # using Django ORM to query database with .get(slug=slug) code
    product = Products.objects.get(slug=slug)
    return render(request, "main/product_detail.html", {"product": product})


@login_required(login_url='login')
def checkout(request):
    return render(request, "main/checkout.html",)


def khalti(request):
    return render(request, "main/khalti.html",)


@login_required(login_url='login')
def cart(request):
    products = Products.objects.all()
    return render(request, "main/cart.html", {"products": products})


@login_required(login_url='login')
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Products.objects.get(id=product_id)
    Carts(user=user, product=product).save()

    return redirect('/cart')


@login_required(login_url='login')
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Carts.objects.filter(user=user)
        amount = 0.0
        # format(amount, ".0")
        # Decimal(amount)
        shipping_amount = 100.0

        cart_product = [p for p in Carts.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = float(p.quantity * p.product.price)
                amount += tempamount
                totalamount = amount + shipping_amount

                return render(request, "main/cart.html", {"carts": cart, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'main/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carts.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        cart_product = [p for p in Carts.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = float(p.quantity * p.product.price)
            amount += tempamount
            totalamount = amount + shipping_amount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount

        }
        return JsonResponse(data)


def minus_cart(request):
    return render


def remove_cart(request):
    return render


def updateItem(request):
    return JsonResponse('ietm was added', safe=False)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'main/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@csrf_exempt
def verify_payment(request):
    data = request.POST
    product_id = data['product_identity']
    token = data['token']
    amount = data['amount']

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "amount": amount
    }
    headers = {
        "Authorization": "Key test_secret_key_dd9644e41839430a8e9e71627b23ce6b"
    }

    response = requests.post(url, payload, headers=headers)

    response_data = json.loads(response.text)
    status_code = str(response.status_code)

    if status_code == '400':
        response = JsonResponse(
            {'status': 'false', 'message': response_data['detail']}, status=500)
        return response

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_data)

    return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}", safe=False)
