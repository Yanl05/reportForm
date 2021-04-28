#-*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/4/20 8:32
# @Author：yanl
# @File    : linkDB.py
# @Software: PyCharm
"""
连接oracle 数据库
"""
# 避免编码问题带来的乱码
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# 连接数据库
from sqlalchemy import create_engine
from util import config

def linkOra():
    engine = create_engine('oracle+cx_oracle://{name}:{pwd}@172.16.20.246:1521/zyyfsyy'.format(name=config.ora_name, pwd=config.ora_pwd))
    return engine

def linkMysql():
    engine = create_engine('mysql+pymysql://{name}:{pwd}@localhost/reportform?charset=utf8'.format(name=config.mysql_name, pwd=config.mysql_pwd))
    return engine


if __name__ == '__main__':
    engine = linkOra()

    with open('../sql/住院药比.sql', 'r', encoding='utf8') as f:
        sqltxt = f.readlines()
        sql3 = "".join(sqltxt)


    import pandas as pd
    df = pd.read_sql(sql3, engine)
    print(df.head())