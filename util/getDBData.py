#-*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/4/20 8:32
# @Author：yanl
# @File    : getDBData.py
# @Software: PyCharm
"""
从oracle / mysql中读取数据
"""
import pandas as pd
from util import linkDB

def getData(sqlfile, DBtype, startdate, enddate):
    """

    :param sqlfile:  包含sql语句的文件
    :param DBtype:  数据库类型 oracle 或者是mysql
    :param startdate:  抽取数据的 开始时间
    :param enddate:    抽取数据的 结束时间
    :return:
    """
    if DBtype == 'oracle':
        engine = linkDB.linkOra()
    elif DBtype == 'mysql':
        engine = linkDB.linkMysql()
    else:
        raise Exception("数据库类型输入错误!!!!", DBtype)

    with open(sqlfile, 'r', encoding='utf8') as f:
        sqltxt = f.readlines()
        sql = "".join(sqltxt)
        sql = sql.format(startdate=startdate, enddate=enddate)
        print(sql)

    df = pd.read_sql(sql, engine)
    # print(df.head())
    return df

# 提供查询
def getData2(sqlfile, DBtype, DBtable,now_time):
    """

    :param sqlfile:  包含sql语句的文件
    :param DBtype:  数据库类型 oracle 或者是mysql
    :param startdate:  抽取数据的 开始时间
    :param enddate:    抽取数据的 结束时间
    :return:
    """
    if DBtype == 'oracle':
        engine = linkDB.linkOra()
    elif DBtype == 'mysql':
        engine = linkDB.linkMysql()
    else:
        raise Exception("数据库类型输入错误!!!!", DBtype)

    with open(sqlfile, 'r', encoding='utf8') as f:
        sqltxt = f.readlines()
        sql = "".join(sqltxt)
        sql = sql.format(now_time=now_time,DBtable=DBtable)
        # print(sql)

    df = pd.read_sql(sql, engine)
    # print(df.head())
    return df

def toMysql(df, DBtable):
    """

    :param df:  数据
    :param DBtable: 表名
    :return:
    """
    engine = linkDB.linkMysql()
    df.to_sql(DBtable, engine, index=False, if_exists='append')
if __name__ == '__main__':
    # oracle 数据库的sql语句文件
    sqlfile = '../sql/住院药比.sql'
    # to mysql 的表名
    DBtable = 'zyyb'

    # 循环输出日期
    import datetime

    start = '2021-01-01'
    end = '2021-04-21'

    datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d')

    while datestart < dateend:
        startdate = datestart.strftime('%Y-%m-%d')
        datestart += datetime.timedelta(days=1)
        enddate = datestart.strftime('%Y-%m-%d')
        df = getData(sqlfile, 'oracle',startdate, enddate)
        toMysql(df, DBtable)
        print(datestart.strftime('%Y-%m-%d'),'   插入成功！！！')

    # df = getData(sqlfile,'oracle')
    # toMysql(df, DBtable)