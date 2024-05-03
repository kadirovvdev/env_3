from django.shortcuts import render
from .models import Category,Computers


def get_info(request):
    category = Category.objects.all()
    context ={
        'category':category
    }
    return render(request,'index.html',context=context)


def get_computers(request,pk):
    computers = Computers.objects.filter(category=pk)
    context ={
        'computers':computers
    }
    return render(request,'computers.html',context=context)


def details(request, pk):
    device = Computers.objects.get(pk=pk)
    context ={
        'device':device
    }
    return render(request,'detail.html',context=context)

# Create your views here.
