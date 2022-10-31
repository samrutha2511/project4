from django.shortcuts import render, redirect
from .forms import BookForm
from . models import Book

# Create your views here.
def home(request):
    book = Book.objects.all()
    context={

        'booklist': book
    }
    return render(request,'home.html',context)

def detail(request,id):
    pd=Book.objects.get(id=id)
    return render(request,'detail.html',{'pd':pd})

def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        pd=Book(bname=name,bdesc=desc,byear=year,bimg=img)
        pd.save()
    return render(request,'add.html')

def update(request,id):
    pd=Book.objects.get(id=id)
    form=BookForm(request.POST or None,request.FILES,instance=pd)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'pd':pd})

def delete(request,id):
    if request.method=='POST':
        pd = Book.objects.get(id=id)
        pd.delete()
        return redirect('/')

    return render(request,'delete.html')

