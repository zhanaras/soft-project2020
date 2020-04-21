from django.urls import path
from api.views import CategoryListAPIView, BrandListAPIView, ProductsTopAPIView, category_products, product_detail, brand_products, orders
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('categories/', CategoryListAPIView.as_view()),
    path('top/', ProductsTopAPIView.as_view()),
    path('categories/<int:category_id>/products/', category_products),
    path('categories/<int:category_id>/products/<int:product_id>/', product_detail),
    path('brands/', BrandListAPIView.as_view()),
    path('brands/<int:brand_id>/products/', brand_products),
    path('orders/', orders)
]