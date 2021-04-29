#-*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/4/20 11:56
# @Author：yanl
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from django.urls import path
from index import views

app_name = 'index'

urlpatterns = [
    url('^$', views.home, name='home'),  # 首页路由
    url('home', views.home, name='home'),  # 首页路由

    url('^yyrb$', views.yyrb, name='yyrb'),  # 医院日报
    url('^mzybbl$', views.mzybbl, name='mzybbl'),  # 门诊药比 比例
    url('^mzyb$', views.mzyb, name='mzyb'),  # 门诊药比

    url('^zyyb$', views.zyyb, name='zyyb'), # 住院药比
    url('^zyybbl$', views.zyybbl, name='zyybbl'), # 住院药比
    url('mzyb', views.mzyb, name='mzyb'), # 门诊药比


    # 获取数据
    url('getZyybData', views.getZyybData, name='getZyybData')  # 获取数据并保存到mysql中

]