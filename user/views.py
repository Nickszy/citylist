from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from user.models import User
# Create your views here.
def index(request):
    return render(request,'user/login.html')

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
            print('chenggong')
        except:
            print('dom')
            return redirect('')
    return redirect('/user/')

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
            return render(request,'index.html')
        else:
            message = '密码不正确！'
            print(message)
            return render(request,'user/login.html',{'message':message})
    return render(request, '/user/login.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/user/")
    request.session.flush()
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return HttpResponseRedirect('../',request)


def register_views(request):
    return render(request,'user/register.html')