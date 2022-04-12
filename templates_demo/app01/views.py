from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    name = 'yuan'
    i = 10
    l = [111,222,333]
    info = {'name':'yuan','age':22}
    b = True
    blank_list = []
    class Person(object):
        def __init__(self,name,age):
            self.name = name
            self.age = age

    alex = Person('alex',333)
    egon = Person('egon',333)
    person_list = [alex,egon]
    text = 'hello python hi luffycity go java linux'
    now = datetime.datetime.now()
    link = "<a href = 'www.baidu.com'>click</a>"



    return render(request,'index.html',locals())

def login(request):
    if request.method == 'POST':
        return HttpResponse("OK!")
    return render(request,'login.html')

def orders(request):

    return render(request,"orders.html")
