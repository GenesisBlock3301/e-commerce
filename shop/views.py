from django.shortcuts import render,HttpResponse
from .models import *
from math import ceil
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import json


def index(request):
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


@login_required
def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Order.objects.filter(order_id=orderId,email=email)
            # return HttpResponse(f"{str(order)}")
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('else')
        except Exception as e:
            return HttpResponse("exception")
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodView(request,id):
    #fetch the product using id
    product = Product.objects.get(id=id)
    # product = get_object_or_404(Product,id=id)
    print(product)
    return render(request, 'shop/prodView.html',{'product':product})

@login_required
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + request.POST.get('address2','')
        city = request.POST.get('city','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        checkout = request.POST.get('checkout','')
        order = Order.objects.create(items_json=items_json,name=name,email=email,address=address ,city=city,zip_code=zip_code,phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,update_desc="The order has been placed.")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html',{'thank':thank,'id':id})
    return render(request, 'shop/checkout.html')
