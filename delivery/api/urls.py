from django.urls import path
from api.views import CategoryListAPIView, CategoryDetailAPIView,BrandListAPIView, ProductDetailAPIView, ProductsTopAPIView, \
    category_products, brand_products, orders, ProductListAPIView, OrderDetailAPIView,BrandDetailAPIView, customers, CustomerDetailAPIView, cards, CardDetailAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),
    path('top/', ProductsTopAPIView.as_view()),
    path('categories/<int:category_id>/products/', category_products),
    path('brands/', BrandListAPIView.as_view()),
    path('brands/<int:brand_id>/', BrandDetailAPIView.as_view()),
    path('brands/<int:brand_id>/products/', brand_products),
    path('orders/', orders),
    path('orders/<int:order_id>/', OrderDetailAPIView.as_view()),
    path('customers/', customers),
    path('customers/<int:customer_id>/', CustomerDetailAPIView.as_view()),
    path('cards/', cards),
    path('cards/<int:card_id>', CardDetailAPIView.as_view())
]