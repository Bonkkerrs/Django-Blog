from django.shortcuts import render, HttpResponse
from app01.models import Book
# Create your views here.
def index(request):
# 增加表记录
# #方式1
#     book_obj = Book(id=1,title='Python',price=100,pub_date='2012-12-12',publish='人民出版社')
#     book_obj.save()
#方式2
    #create方法返回对象（一条添加的记录）
    # book_obj = Book.objects.create(title='Calculus',price=50,pub_date='2000-12-01',publish='SJTU')
    # print(book_obj.__dict__)

#查询表记录
    # book_list = Book.objects.all()
    # print(book_list)
    # print(book_list.first())
    # print(book_list.last())
    # print(Book.objects.filter(price=100))
    # print(Book.objects.get(title='Python'))
    print(Book.objects.exclude(title='Python'))
    return HttpResponse('OK!')