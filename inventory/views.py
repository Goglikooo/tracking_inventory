from django.shortcuts import render, redirect
from .models import Inventory
# Create your views here.

def main(request):
    inventory = Inventory.objects.all()
    return render(request, 'index.html', {'inventory': inventory})

def table(request):
    inventory = Inventory.objects.all()
    return render(request, 'table.html', {"inventory":inventory })

def add_item(request):
    if request.method =="POST":
        new_item = Inventory(
            name = request.POST.get('name'),
            serial_number = request.POST.get('serial_number'),
            price= request.POST.get('price')
        )
        new_item.save()
        return redirect('index')
    else:
        return render(request, 'add.html')
    

def edit_item(request, id):
    item = Inventory.objects.get(name=id)
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.serial_number = request.POST.get('serial_number')
        item.price = request.POST.get('price')
        item.save()
        return redirect('index')
    else:
        return render(request, 'edit.html', {'item': item})
