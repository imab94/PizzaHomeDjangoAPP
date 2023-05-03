from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="indexpage"),
    path("addtocart/",views.addtocart,name="addtocart"),
    path("add_toppings/",views.add_toppings,name="add_toppings"),

]