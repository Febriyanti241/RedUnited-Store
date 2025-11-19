from django.urls import path
from authentication.views import login, logout, register, create_product_flutter, show_my_products_json

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json/my-products/', show_my_products_json, name='show_my_products_json'),
    path('logout/', logout, name='logout'),
]