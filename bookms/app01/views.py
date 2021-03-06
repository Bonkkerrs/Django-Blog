from django.shortcuts import render, HttpResponse, redirect
from app01.models import *
# Create your views here.
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        book_obj = Book.objects.create(title=title,price=price,pub_date=date,publish=publish)
        return redirect('/books')
    else:
        return render(request,'addbook.html')

def books(request):
    book_list = Book.objects.all()
    return render(request,'books.html',locals())

def delbook(request,id):
    Book.objects.filter(id=id).delete()
    return redirect("/books")

def edit(request,id):
    book_obj = Book.objects.filter(id=id).first()
    if request.method == 'GET':
        return render(request,'edit.html',locals())
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        Book.objects.filter(id=id).update(title=title,price=price,pub_date=date,publish=publish)
        return redirect('/books')