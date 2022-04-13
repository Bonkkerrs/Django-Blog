from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import widgets
from app01.models import UserInfo
from django.core.exceptions import ValidationError
# Create your views here.
class UserForm(forms.Form):
    name = forms.CharField(min_length=4,label='姓名',widget=widgets.TextInput(attrs={"class":"form-control"}))
    pwd = forms.CharField(min_length=4,label='密码',widget=widgets.PasswordInput(attrs={"class":"form-control"}))
    pwd2 = forms.CharField(min_length=4,label='确认密码',widget=widgets.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='邮箱',widget=widgets.TextInput(attrs={"class":"form-control"}))
    tel = forms.CharField(label='手机号',widget=widgets.TextInput(attrs={"class":"form-control"}))

    def clean_name(self):
        val = self.cleaned_data.get("name")
        ret = UserInfo.objects.filter(name=val)
        if not ret:
            return val
        else:
            raise ValidationError("该用户已注册！")

    def clean_tel(self):
        val = self.cleaned_data.get("tel")
        if len(val) == 11:
            if val.isdigit():
                return val
            else:
                raise ValidationError("请填入正确的手机号！")
        else:
            raise ValidationError("请填入正确的手机号！")

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        pwd2 = self.cleaned_data.get("pwd2")
        if pwd == pwd2:
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        else:
            print(form.cleaned_data)
            print(form.errors)
            errors = form.errors.get("__all__")
            return render(request, 'login.html', locals())

        return HttpResponse('OK')
    form = UserForm()
    return render(request,'login.html',locals())