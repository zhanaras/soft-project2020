from rest_framework import serializers
from api.models import Category, Brand, Product, Order, Employee


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'description', 'ingredients', 'price', 'brand', 'category', 'barcode', 'quantity', )

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'name', 'address', 'phone', 'products', 'isActive', )

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'id_number', 'address', 'phone',  'age', 'gender', 'salary', )