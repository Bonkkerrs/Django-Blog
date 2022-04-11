from django.shortcuts import render
from django.http import HttpResponse
import datetime
#反向解析函数
from django.urls import reverse
# Create your views here.
def index(request):
    print(request.method)
    return render(request,'index.html',{'title':'My Title'})



def login(request):
    #如果是GET请求就返回页面，如果是POST请求就校验
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        print(request.POST)
        user = request.POST.get("user")
        pwd = request.POST.get('pwd')
        return render(request,'app01:login.html')

def special_case_2003(request):
    c_time = datetime.datetime.now()
    reverse()
    return HttpResponse(f"{c_time}")

def month_archive(request,m,y):
    print(m,type(m))
    print(y,type(y))
    return HttpResponse('OK!')

def path_year(request,year):
    print(type(year))
    return HttpResponse("Path OK!")

def path_month(request,month):
    print(type(month))
    return HttpResponse("Converter Path OK!")

