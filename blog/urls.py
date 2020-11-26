from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="bogHome"),
    path("blpost/<int:id>", views.blogpost, name="blogpost")

]
