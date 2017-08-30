"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse,render,redirect
def login(request):
    """
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息(对象)
    :return:
    """
    # return HttpResponse('HttpResponse里只能返回字符串')
    if request.method=="GET":
        return render(request,'login.html') #通过render返回渲染后的html文件
    else:
        #request.POST用户POST提交的数据（请求体）
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        if u=='root' and p=='123123':
            return redirect('http://www.oldboyedu.com')
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误!'})
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
]