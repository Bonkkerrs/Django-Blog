from django.shortcuts import render, HttpResponseRedirect
from app01 import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def timer(request):
    return render

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')

def index(request):
    return render(request,'base.html',{'category_list':category_list})

def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    return render(request,'base.html',{'category_list':category_list,
                                       'category_obj':category_obj})

def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or '/')
        else:
            login_err = "Wrong username or password!"
            return render(request,'login.html',{'login_err':login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')