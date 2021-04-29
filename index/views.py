from django.http import HttpResponse
from django.shortcuts import render, redirect
from util import linkDB, getDBData
import json
import os
import pandas as pd
from util.getDBData import getData2,getData,toMysql

# Create your views here.

def home(request):
    return render(request, 'home.html')

def yyrb(request):
    if request.method == 'GET':
        return render(request, 'yyrb.html')
    else:
        dataset = 111
        return HttpResponse(dataset, content_type="application/json")

def mzybbl(request):
    pass


def zyyb(request):
    if request.method == 'GET':
        return render(request, 'zyyb.html')
    elif request.method == 'POST':
        starttime = request.POST.get("time")[:10]
        endtime = request.POST.get("time")[13:]
        # windows下路径
        # sqlfile = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sql\住院药比金额mysql.sql')
        # mac环境下路径
        sqlfile = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sql/住院药比金额mysql.sql')
        # print(sqlfile)
        df = getDBData.getData(sqlfile, 'mysql', starttime, endtime)
        dataset = df.to_json(orient="table", force_ascii=False)
        datadict = json.loads(dataset)
        # 添加状态信息，状态为1 为检索成功。状态为0 为检索失败
        datadict["status"] = 1
        dataset = json.dumps(datadict)
        print("sql查询成功！！！！！！！！！")
        return HttpResponse(dataset, content_type="application/json")

def zyybbl(request):
    if request.method == 'GET':
        return render(request, 'zyybbl.html')
    elif request.method == 'POST':
        starttime = request.POST.get("time")[:10]
        endtime = request.POST.get("time")[13:]
        # windows下路径
        # sqlfile = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sql\住院药比金额mysql.sql')
        # mac环境下路径
        sqlfile = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sql/住院药比比例mysql.sql')
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

def getZyybData(request):
    if request.method == 'GET':
        # dataset = json.dumps("请提交数据")
        dataset = "请提交数据"
        return HttpResponse(dataset, content_type="text/html;charset=UTF-8")
    elif request.method == 'POST':
        req = json.loads(request.body)
        print(req)
        DBtable = 'zyyb'
        df = pd.read_json(req, orient='index')
        # 由于科室编码 有部分为 0 开头的 对此进行处理
        df['dept_code'] = [i[1:5] for i in df['dept_code']]
        # print(df)
        now_time = df['create_date'][0]
        # 判断该日期是否有数据
        sqlfile1 = './sql/查询某日期表中是否有数据.sql'
        res = getData2(sqlfile1, 'mysql', DBtable, now_time)
        # 先判断表中是否有该天的数据，如果有 则不抽取数据
        if len(res) == 0:
            try:
                toMysql(df, DBtable)
                print('住院药比 --- 数据插入成功 ')
            except Exception as e:
                print('住院药比 --- 数据插入失败！！！！ ')
        else:
            print(now_time, "   -----该日期已有数据")

        return HttpResponse(req, content_type= 'text/html;charset=UTF-8')



def getdataeveryday():
    print('定时任务...')