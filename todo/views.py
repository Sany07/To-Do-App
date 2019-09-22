from django.shortcuts import render,redirect
from .form import ListForm
from .models import List
from django.contrib import messages

def home(request):
    try:
        if request.method == 'POST':
            form=ListForm(request.POST or None)
            if form.is_valid():
                form.save()
                context={
                    'all_items':List.objects.order_by('-id')
                }
                messages.success(request,('Item Has Been Added'))
                return render(request,'index.html',context)

    except:
         messages.error(request,('Input Data'))
        
    context={
                    'all_items':List.objects.order_by('-id')
                }
    return render(request,'index.html',context)


def delete(request , id):

    items=List.objects.get(id=id)
    items.delete()
    messages.success(request,('Item Has Been Deleted'))
    return redirect('home')


def edit(request,id):
    if request.method == 'POST':
        item=List.objects.get(pk=id)
        form=ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            
            messages.success(request,('Item Has Been Added'))
            return redirect('home')
    else:
        item=List.objects.get(pk=id)
        context={
                'item':item
            }
        return render(request,'edit.html',context)   


def cross_off(request,id):
    item=List.objects.get(id=id)
    item.completed=True
    item.save()
    return redirect('home')


def uncross(request,id):
    item=List.objects.get(id=id)
    item.completed=False
    item.save()
    return redirect('home')