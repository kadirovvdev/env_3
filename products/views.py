from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Category,Computers


def get_info(request):
    category = Category.objects.all()
    context ={
        'category': category
    }
    return render(request,'index.html',context=context)


def get_computers(request,pk):
    computers = Computers.objects.filter(category=pk)
    context ={
        'computers': computers
    }
    return render(request,'computers.html',context=context)


def details(request, pk):
    device = Computers.objects.get(pk=pk)
    context ={
        'device':device
    }
    return render(request,'detail.html',context=context)


def add_products(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = Category.objects.get(pk=pk)
    form = Category(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('products:get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)

# Create your views here.
