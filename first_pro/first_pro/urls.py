"""first_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, register_converter
from app01 import views
from app01.urlconvert import MonConvert
# 自定义path匹配器    先注册转换器
register_converter(MonConvert,"mm")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name='Log'), #反向解析，起别名
    re_path('^article/2003/$',views.special_case_2003,name="s_c_2003"),
    re_path('^article/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})$',views.month_archive),
    path("article/<int:year>",views.path_year),
    path("article/<mm:month>",views.path_month),
    re_path(r"index/",views.index)
]
