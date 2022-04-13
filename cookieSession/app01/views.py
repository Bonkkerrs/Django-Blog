from django.shortcuts import render, HttpResponse
from app01.models import UserInfo
# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(name=name,pwd=pwd)
        if user:
            response = HttpResponse("登录成功")
            response.set_cookie("is_login",True)
            return response
    return render(request,'login.html')

def index(request):
    print(request.COOKIES)
    is_login = request.COOKIES.get("is_login")
    if is_login:
        return render(request,'index.html')
    else:
        return render(request,'login.html')