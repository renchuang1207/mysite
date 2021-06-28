"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import HttpResponse, render, redirect
from django.urls import path
from django.conf.urls import url
from utils.pymsql_utils import py


def login(request):
    """
    处理用户请求，并返回内容
    @param request:用户请求相关的所有信息（对象）
    @return:
    """
    # return HttpResponse('')
    #自动找到模版路径下的login.html
    if request.method == 'GET':
        return render(request,'login.html',{"msg":"123123"})
    else:
        #用户POST提交的请求体
        u = request.POST.get('username')
        p = request.POST.get('password')
        up = u + '|' + p
        sql_user = 'select username,password from user'
        res_user_list = py.select_sql(sql_user)
        # print(up)
        # print(res)
        username_password_list = [item['username']+'|'+item['password'] for item in res_user_list]
        # print(username_password_list)
        if up in username_password_list:
            
            # return render(request,'index.html',{'student_list':res_student_list})
            return redirect('/index/')
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误'})
        
        
def index(request):
    sql_student = 'select Sid,Sname,Sage from student'
    res_student_list = py.select_sql(sql_student)
    return render(request,
                  'index.html',
                  {
                      'name':'alex',
                      'users':['李志','李杰'],
                      'user_dict':{'k1':'v1','k2':'v2'},
                      'user_list_dict':[
                          {'id':1,'name':'alex','email':'alex3714@163.com'},
                          {'id':2,'name':'alex1', 'email': 'alex3714@163.com'},
                          {'id':3,'name':'alex2', 'email': 'alex3714@163.com'},
                      ],
                      'student_list': res_student_list
                  })


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/',login),
    url(r'^index/',index),
]
