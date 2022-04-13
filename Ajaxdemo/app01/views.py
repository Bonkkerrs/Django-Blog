from django.shortcuts import render, HttpResponse
from app01.models import User
import json
# Create your views here.
def index(request):
    return render(request,'index.html')

def test_ajax(request):
    print(request.GET)
    return HttpResponse('OK')

def cal(request):
    n1 = request.POST.get("n1")
    n2 = request.POST.get('n2')
    ret = int(n1)+int(n2)
    return HttpResponse(f"{ret}")

def login(request):
    print(request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get('pwd')
    user = User.objects.filter(name=user,pwd=pwd).first()
    res = {
        "user":None,
        "msg":None
    }
    if user:
        res['user'] = user.name
    else:
        res['msg'] = "Username or password wrong!"
    return HttpResponse(json.dumps(res))


def upload(request):
    if request.method == 'POST':
        print(request.POST)

        # print(request.FILES)
        # file_obj = request.FILES.get("file")
        # with open(file_obj.name,'wb') as f:
        #     for line in file_obj:
        #         f.write(line)

        return HttpResponse('OK')
    print('GET!')
    return render(request,'upload.html')
