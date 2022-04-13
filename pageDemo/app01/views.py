from django.shortcuts import render, HttpResponse
import numpy as np
from app01.models import Book
# Create your views here.
from django.core.paginator import Paginator, EmptyPage
def index(request):
    # arr = np.random.randn(100)
    # for i in range(100):
    #     book_obj = Book.objects.create(title='book%s'%i,price=arr[0])
    #     book_obj.save()
    book_list = Book.objects.all()



    try:
        page = int(request.GET.get('page',1))
        current_page = int(request.GET.get('page',1))
        paginator = Paginator(book_list,10)
        c_page = paginator.page(current_page)
        print(paginator.page(1).object_list)
        current_page = paginator.page(current_page).object_list

    except EmptyPage:
        current_page = paginator.page(1).object_list
    return render(request,'index.html',locals())