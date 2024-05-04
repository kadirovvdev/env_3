from django.urls import path
from .views import get_info,get_computers,details,add_products,update_products

urlpatterns = [
    path('',get_info,name='info'),
    path('computers/<int:pk>', get_computers, name='computers'),
    path('details/<int:pk>',details,name='details'),
    path('add_products', add_products, name='add_products'),
    path('update/<int:pk>', update_products, name='update'),
    ]