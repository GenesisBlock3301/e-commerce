from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=55,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images',default="")
    desc = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=88)
    email = models.CharField(max_length=88)
    address = models.CharField(max_length=88)
    city = models.CharField(max_length=88)
    state = models.CharField(max_length=88)
    zip_code = models.CharField(max_length=88)
    phone = models.CharField(max_length=88,default='')


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:2]+"..."

