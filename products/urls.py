from django.urls import path
from .views import get_info,get_computers,details

urlpatterns = [
    path('',get_info,name='info'),
    path('computers/<int:pk>', get_computers, name='computers'),
    path('details/<int:pk>',details,name='details')
    ]