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


def city(request):
    city_name = request.GET.get('city','')
    if City.objects.filter(city__contains=city_name):
        print(city)
        content={
            'city':{
                'name': city_name,
                'people': 213123,
            }
        }
        content['lasttime'] = '2020-03-01'
        return render(request, './city/city.html', content)
    return render(request,'./404.html')

def env(request):
    return render(request,'./city/chart.html')

def citylist(request):
    content={'citylist':{}}
    city_des = City.objects.all()
    for city in city_des[0:20]:
        content['citylist'][f'{city.city}'] = {
            'name': city.city, 'tags': city.tags, 'des': city.des,'address':'/'.join([str(city.province),str(city.city)]).replace('None','')+'/'}
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

