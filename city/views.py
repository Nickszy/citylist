import json
from random import randrange

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from pyecharts.charts import Bar
from pyecharts import options as opts

def index(request):
    return render(request,'index.html')


def city(request):
    city = request.GET.get('city','')
    list = ['上海','湖州']
    if city in list:
        content={
            'city':{
            'name': city,
            'people': 213123,
            }}
        content['lasttime'] = '2020-03-01'
        return render(request, './city/city.html',content)
    return render(request,'./404.html')

def env(request):
    return render(request,'./city/chart.html')

def citylist(request):
    content = {
        'citylist':{
            'dadas':{'name':'上海','place':'🌲🌊🌊','address':'上海市','tags':'国际化 魔都'},
            'dadd':{'name':'上海','place':'🌲🌊🌊','address':'上海市','tags':'国际化 魔都'},
            's':{'name':'上海','place':'🌲🌊🌊','address':'上海市','tags':'国际化 魔都'},
            'dasd':{'name':'上海','place':'🌲🌊🌊','address':'上海市','tags':'国际化 魔都'},
            'dsad':{'name':'上海','place':'🌲🌊🌊','address':'上海市','tags':'国际化 魔都'},
            'huzhou': {'name':'湖州','place':"🏔🌲🌊",'address':'浙江省/湖州市','tags':'长三角 南太湖'}
        }
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
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="对比", subtitle="杭州vs湖州"))
        .dump_options_with_quotes()
    )
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))


