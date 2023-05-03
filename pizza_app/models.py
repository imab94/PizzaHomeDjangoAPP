from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CrousalMedia(models.Model):
    name= models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='pizza_app/images', default="")
    def __str__(self):
        return str(self.name)

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    # SIZE_CHOICES = [
    #     ('REGULAR', 'Regular'),
    #     ('MEDIUM', 'Medium'),
    #     ('LARGE', 'Large'),
    # ]
    CATEGORY_CHOICES = [
        ('VEG', 'Veg'),
        ('NON_VEG', 'Non-Veg'),
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='snippets/images', default="")
    description = models.CharField(max_length=200,blank=True)
    # size = models.CharField(choices=SIZE_CHOICES, max_length=7)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=7)
    # toppings = models.ManyToManyField(Topping, related_name='pizzas', blank=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

    