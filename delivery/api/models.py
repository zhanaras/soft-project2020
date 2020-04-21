from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)


class Brand(models.Model):
    title = models.CharField(max_length=300)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    barcode = models.IntegerField(blank=False, null=True, unique=True)
    quantity = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    description = models.TextField(default='')
    ingredients = models.TextField(default='')
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_list')


class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    products = models.ManyToManyField(Product)
    isActive = models.BooleanField(default=True)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id_number = models.IntegerField(blank=False, null=True, unique=True)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    salary = models.FloatField()
# Create your models here.
