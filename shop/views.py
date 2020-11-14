from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from math import ceil
from django.shortcuts import get_object_or_404

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
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        # print(name,email,phone,desc)
        contact = Contact.objects.create(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodView(request,id):
    #fetch the product using id
    product = Product.objects.get(id=id)
    # product = get_object_or_404(Product,id=id)
    print(product)
    return render(request, 'shop/prodView.html',{'product':product})


def checkout(request):
    return render(request, 'shop/checkout.html')
