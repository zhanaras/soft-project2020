from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Category, Brand, Product, Order
from api.serializers import CategorySerializer, BrandSerializer, ProductSerializer, OrderSerializer


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status

class CategoryListAPIView(mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductListAPIView(mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BrandListAPIView(mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductsTopAPIView(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = Product.objects.order_by('-price')[:15]
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def category_products(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        products = category.product_list.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def brand_products(request, brand_id):
    try:
        brand = Brand.objects.get(id = brand_id)
    except Brand.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        products = brand.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def product_detail(request, category_id, product_id):
    try:
        category = Category.objects.get(id = category_id)
        product = category.product_list.get(id=product_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'deleted': True})

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def orders(request):
    try:
        orders = Order.objects.all()
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(instance = orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        orders.delete()
        return Response({'deleted': True})

# class VacancyDetailAPIView(generics.RetrieveDestroyAPIView):
#     queryset = Vacancies.objects.all()
#     serializer_class = VacancySerializer
#
#
# class VacancyTopTenAPIView(mixins.ListModelMixin,
#                            generics.GenericAPIView):
#     queryset = Vacancies.objects.order_by('-salary')[:10]
#     serializer_class = VacancySerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
# Create your views here.
