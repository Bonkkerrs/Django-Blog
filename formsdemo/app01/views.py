from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import widgets
# Create your views here.
class UserForm(forms.Form):
    name = forms.CharField(min_length=4,label='姓名',widget=widgets.TextInput(attrs={"class":"form-control"}))
    pwd = forms.CharField(min_length=4,label='密码',widget=widgets.PasswordInput(attrs={"class":"form-control"}))
    pwd2 = forms.CharField(min_length=4,label='确认密码',widget=widgets.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='邮箱',widget=widgets.TextInput(attrs={"class":"form-control"}))
    tel = forms.CharField(label='手机号',widget=widgets.TextInput(attrs={"class":"form-control"}))




def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        else:
            print(form.cleaned_data)
            print(form.errors)
            return render(request, 'login.html', locals())

        return HttpResponse('OK')
    form = UserForm()
    return render(request,'login.html',locals())