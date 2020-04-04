import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from user.models import *
# Create your views here.
def index(request):
    return render(request,'user/login.html')

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]#所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
    return ip

def register(request):
    uname = request.POST.get('uname','')
    if User.objects.filter(uname=uname):
        return redirect('/user/')
    else:
        new_user = User()
        try:
            new_user.uname = uname
            new_user.upass = request.POST.get('upass',)
            new_user.uemail = request.POST.get('uemail',)
            new_user.save()
            # 将用户信息存在session中
            user = User.objects.get(uname=uname)
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.uname
            # 记录用户注册时间
            ureg = User_login(ip=get_ip(request), user_id=user.id, time=datetime.datetime.now(),
                                 status='register')
            ureg.save()
            message = '注册成功，请登录'
        except:
            return render(request,'/user/login.html',{'message':'请重新输入'})
    return render(request,'user/login.html',{'message':message})

def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        message = '不允许重复登录'
        return render(request,'user/login.html',{'message':message})
    if request.method == 'POST':
        message = '请检查填写的内容！'
        uname = request.POST.get('uname','')
        password = request.POST.get('upass','')
        try:
            user = User.objects.get(uname=uname)
        except :
            message = '用户不存在！'
            return render(request,'user/login.html',{'message':message})
        if user.upass == password:
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.uname
            #记录用户登录时间
            ulogin = User_login(ip=get_ip(request),user_id=user.id,time=datetime.datetime.now(),status='login')
            ulogin.save()
            return HttpResponseRedirect('../')
        else:
            message = '密码不正确！'
            print(message)
            return render(request,'user/login.html',{'message':message})
    return render(request, '/user/login.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/user/")
    #记录用户登出时间
    ulogout = User_login(ip=get_ip(request), user_id=request.session['user_id'], time=datetime.datetime.now(),
                         status='logout')
    ulogout.save()
    request.session.flush()
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return HttpResponseRedirect('../',request)


def register_views(request):
    return render(request,'user/register.html')


def dashboard(request):
    return render(request,'user/dashboard.html')