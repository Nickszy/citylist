import datetime
import json
from random import randrange

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from pyecharts.charts import Bar
from pyecharts import options as opts
from city.models import *

def index(request):
    return render(request,'index.html')

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]#所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
    return ip

def city(request):
    city_name = request.GET.get('city','')
    if City.objects.filter(city__contains=city_name):
        city_des = City.objects.get(city=city_name)
        city_des.click_num+=1
        content={
            'city':{
                'name': city_des.city,
                'people': 213123,
                'province':city_des.province,
                'lng': city_des.lng,
                'lat': city_des.lat
            }
        }
        content['lasttime'] = '2020-03-01'
        city_des.save()
        if request.session.get('is_login', None):
            click = City_click(user_id=request.session['user_id'],time=datetime.datetime.now(),city=city_name,city_id = city_des.id,ip=get_ip(request))
        else:
            click = City_click(user_id=None,time=datetime.datetime.now(),city=city_name,city_id = city_des.id,ip=get_ip(request))
        click.save()
        return render(request, './city/city.html', content)
    return render(request,'./404.html')

def env(request):
    return render(request,'./city/chart.html')

def citylist(request):
    content={'citylist':{}}
    data = City.objects.all()
    city_des = data.order_by('-click_num')
    for city in city_des[0:20]:
        content['citylist'][f'{city.city}'] = {
            'name': city.city,
            'tags': city.tags,
            'des': city.des,
            'address':'/'.join([str(city.province),str(city.city)]).replace('None','')+'/',
            # 'click_num': city.click_num
            'click_num':Count.objects.get(city=city.city).count_city_click_num,
        }
    return render(request, './city/citylist.html',content)


def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error

def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["郊游", "自行车","宠物", "老年人"])
        .add_yaxis("湖州", [randrange(0, 10) for _ in range(4)])
        .add_yaxis("杭州", [randrange(0, 10) for _ in range(4)])
        .set_global_opts(title_opts=opts.TitleOpts(title="友好度", subtitle="杭州vs湖州"))
        .dump_options_with_quotes()
    )
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))

