# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个DaShare服务应用风机路由类，主要使用fastapi搭建ASGI服务器
"""
模块介绍
-------

这是一个DaShare服务应用气象路由类，主要使用fastapi搭建ASGI服务器

设计模式：

    无

关键点：    

    （1）fastapi

主要功能：            

    （1）DaShare服务应用风机路由
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fastapi import APIRouter
from dashare.util.info_tool import get_dashare_metadb_connection,encrypt_password
from dashare.util.token_tool import encode_token,get_user_token,decode_token
from dashare.util.trafic_tool import get_user_trafic,set_user_trafic
from dashare.util.request_tool import collect_params,request_pretreate,get_data
from dashare.service.dbconnection import db_engine
from dashare.service.cons import WIND_TURBINE_DATA_DICT
import pandas as pd
import datetime
import time
import json



####### DaShare服务应用风机路由 ##############################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）fastapi                                                          ###
### 主要功能：                                                            ###
### （1）DaShare服务应用-风机数据管理                                      ###
############################################################################



###### DaShare服务应用风机数据路由操作 #####################################################################
##########################################################################################################



### 创建fastapi应用实例-风机路由
wind_turbine_router = APIRouter()


### 获取风机数据路由
### 获取风机数据
@wind_turbine_router.get("/get_wind_turbine_data")
async def get_wind_turbine_data(token_key,token,entity,start_time,end_time):
    '''
    函数功能：

        定义一个获取风机数据的函数，主要提供风机数据

    参数：
        token_key (str): token密钥
        token (str): token串
        entity (str): 数据实体
        start_time (str): 数据开始时间
        end_time (str): 数据结束时间

    返回：
        tmp_json (json): json结果字符串
    '''

    start_time = start_time.replace(',',' ')
    end_time = end_time.replace(',',' ')
    entity = str(entity)
    ### 开始预处理
    pretreatment = request_pretreate(token_key=token_key,token=token)
    print(pretreatment)
    ### 收集查询语句，从dashare.service.cons中
    select_sql = WIND_TURBINE_DATA_DICT[entity].format(start_time=start_time,end_time=end_time)
    ### 执行获取数据辅助函数，该函数主体主要分为两步，第一步：判断用户和数据情况；第二步：根据不同情况输出具体数据
    tmp_json = get_data(pretreatment=pretreatment,select_sql=select_sql,start_time=start_time,end_time=end_time)
    print('===========================================')
    print(tmp_json)

    return tmp_json 



####################################################################################################################
####################################################################################################################


