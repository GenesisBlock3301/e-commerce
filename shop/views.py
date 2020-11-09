from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from math import ceil


def index(request):
    # products = Product.objects.all()
    # params = {
    #     'products': products,
    # }
    # all_Prods = [[products],[products]]
    # params = {
    #     'allProds':all_Prods
    # }
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)



def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("we are at contact")


def tracker(request):
    return HttpResponse("we are at tracker")


def search(request):
    return HttpResponse("we are at search")


def prodView(request):
    return HttpResponse("we are at prodView")


def checkout(request):
    return HttpResponse("we are at checkout")
