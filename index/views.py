from django.http import HttpResponse
from django.shortcuts import render, redirect
from util import linkDB, getDBData
import json
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')


def zyyb(request):
    if request.method == 'GET':
        return render(request, 'zyyb.html')
    elif request.method == 'POST':
        starttime = request.POST.get("time")[:10]
        endtime = request.POST.get("time")[13:]
        sqlfile = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),'sql\住院药比mysql.sql')
        # print(sqlfile)
        df = getDBData.getData(sqlfile, 'mysql', starttime, endtime)
        dataset = df.to_json(orient="table", force_ascii=False)
        datadict = json.loads(dataset)
        # 添加状态信息，状态为1 为检索成功。状态为0 为检索失败
        datadict["status"] = 1
        dataset = json.dumps(datadict)
        print("sql查询成功！！！！！！！！！")
        return HttpResponse(dataset, content_type="application/json")

def mzyb(request):
    pass

def


def getdataeveryday():
    print('定时任务...')