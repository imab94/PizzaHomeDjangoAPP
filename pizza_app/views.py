from django.shortcuts import render
from .models import Topping,Pizza,CrousalMedia,Size

# Create your views here.

def index(request):
    # for i in t:
    #     print(i.veg_pizza,i.non_veg_pizza,i.topping.name,i.topping.price)
    images = CrousalMedia.objects.all()
    pizza = Pizza.objects.all()
    # print(list(pizza)) 
    sizes = Size.objects.all()
    toppings = Topping.objects.all()
    # print(list(sizes))
    return render(request,'pizza_app/index.html',{'images':images,'pizza_menu':pizza,'pizza_objects':sizes,'toppings':toppings})

def addtocart(request):
    pizza_name = request.GET.get('pizza_name', '')
    return render(request,'pizza_app/addtocart.html',{'pizza_name':pizza_name})

def add_toppings(request):
    toppings = Topping.objects.all()
    #context = {'pizza_name': pizza_name}
    pizza_name = request.GET.get('pizza_name', '')
    return render(request,'pizza_app/add_toppings.html',{'toppings':toppings,'pizza_name':pizza_name})
