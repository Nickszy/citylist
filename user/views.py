from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user/login.html')


def login(request):
    uname = request.POST.get('uname','')
    upass = request.POST.get('upass','')
    print(uname,upass)
    if uname and upass:
        response = HttpResponse()
        return response
    return HttpResponseRedirect('/user/')