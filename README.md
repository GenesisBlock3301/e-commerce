# E-commerce

## Setup Project

```
django-admin startproject e-commerce
```
# index view
```python
>>>
for i in cats:
    ...:     prod = Product.objects.filter(category=i)
    ...:     n = len(prod)
    ...:     nslides = n//4 + ceil((n/4)-(n//4))
    ...:     allprods.append([prod,range(1,nslides),nslides])

[[<QuerySet [<Product: Watch>]>, range(1, 1), 1],
 [<QuerySet [<Product: Rice Cooker>, <Product: Mobile>]>, range(1, 1), 1],
 [<QuerySet [<Product: Fan>]>, range(1, 1), 1],
 [<QuerySet [<Product: Laptop>]>, range(1, 1), 1]]

```
