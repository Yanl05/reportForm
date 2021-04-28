#-*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/4/21 15:17
# @Author：yanl
# @File    : shcedulerGetData.py
# @Software: PyCharm
# oracle 数据库的sql语句文件
"""
定时获取数据插入 mysql
  插入之前先判断是否有数据 有就不插入
"""
import datetime
from getDBData import getData2,getData,toMysql
def getdataeveryday():
    sqlfile1 = '../sql/查询某日期表中是否有数据.sql'

    sqlfile2 = '../sql/住院药比.sql'
    # to mysql 的表名
    DBtable = 'zyyb'

    # now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # end_tiem = datetime.datetime.now() + datetime.timedelta(days=1)
    # end_tiem = end_tiem.strftime('%Y-%m-%d')

    now_time = '2021-04-20'
    end_tiem = '2021-04-21'


    df = getData2(sqlfile1,'mysql', DBtable,now_time)
    # 先判断表中是否有该天的数据，如果有 则不抽取数据
    if len(df) == 0:
        df = getData(sqlfile2, 'oracle', now_time, end_tiem)
        toMysql(df, DBtable)
        print(now_time, '  -----定时任务  插入成功！！！')
    else:
        print(now_time, "   -----定时任务未执行")

    # start = '2021-01-01'
    # end = '2021-04-21'
    #
    # datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    # dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
    #
    # while datestart < dateend:
    #     startdate = datestart.strftime('%Y-%m-%d')
    #     datestart += datetime.timedelta(days=1)
    #     enddate = datestart.strftime('%Y-%m-%d')
    #     df = getData(sqlfile, 'oracle', startdate, enddate)
    #     toMysql(df, DBtable)
    #     print(datestart.strftime('%Y-%m-%d'), '   插入成功！！！')
if __name__ == '__main__':
    getdataeveryday()