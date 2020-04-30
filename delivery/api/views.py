from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Category, Brand, Product, Order, Customer, Card
from api.serializers import CategorySerializer, BrandSerializer, ProductSerializer, OrderSerializer, CustomerSerializer, CardSerializer


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

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, category_id):
        category = self.get_object(category_id)
        category.delete()

        return Response({'deleted': True})


class ProductListAPIView(mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()

        return Response({'deleted': True})


class BrandListAPIView(mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BrandDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Brand.objects.get(id=id)
        except Brand.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, brand_id):
        brand = self.get_object(brand_id)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, brand_id):
        brand = self.get_object(brand_id)
        serializer = BrandSerializer(instance=brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, brand_id):
        brand = self.get_object(brand_id)
        brand.delete()

        return Response({'deleted': True})


class ProductsTopAPIView(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = Product.objects.order_by('-price')[:15]
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def category_products(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
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


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def orders(request):
    try:
        orders = Order.objects.all()
    except Order.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(instance=orders, data=request.data)
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


class OrderDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, order_id):
        order = self.get_object(order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, order_id):
        order = self.get_object(order_id)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, order_id):
        order = self.get_object(order_id)
        order.delete()

        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def customers(request):
    try:
        customers = Customer.objects.all()
    except Customer.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(instance=customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})


class CustomerDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, customer_id):
        customer = self.get_object(customer_id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, customer_id):
        customer = self.get_object(customer_id)
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, customer_id):
        customer = self.get_object(customer_id)
        customer.delete()

        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def cards(request):
    try:
        cards = Card.objects.all()
    except Card.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CardSerializer(instance=cards, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})


class CardDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Card.objects.get(id=id)
        except Card.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, card_id):
        card = self.get_object(card_id)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, card_id):
        card = self.get_object(card_id)
        serializer = CardSerializer(instance=card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, card_id):
        card = self.get_object(card_id)
        card.delete()

        return Response({'deleted': True})

# Create your views here.
