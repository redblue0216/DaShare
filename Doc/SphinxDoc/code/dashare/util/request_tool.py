# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个DaShare的request工具类，主要功能提供收集信息功能
"""
模块介绍
-------

这是一个DaShare的request工具类，主要功能提供收集信息功能

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）收集信息功能
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import pandas as pd
import datetime
import time
import jwt 
import json
from dashare.util.info_tool import get_dashare_metadb_connection,encrypt_password
from dashare.util.token_tool import encode_token,get_user_token,decode_token
from dashare.util.trafic_tool import get_user_trafic,set_user_trafic
from dashare.service.dbconnection import db_engine




####### DaShare的token工具类 ################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）收集信息功能                                                     ###
############################################################################



###### DaShare的request工具操作 #######################################################################
######################################################################################################



### 收集参数
def collect_params(token_key,token):
    '''
    函数功能：

        定义一个收集参数的函数

    参数：
        token_key (str): token密钥
        token (str): token字符串

    返回：
        result (dict): 结果字典
    '''

    ### 收集参数阶段，使用try-except异常捕捉
    result = {}
    try:
        ### 收集参数，包括token_key和token
        token_key = str(token_key)
        token = str(token)
        encoded_jwt = token
        SECRET_KEY = token_key
        ### 解析jwt-token
        decoded_jwt = decode_token(encoded_token=encoded_jwt,key=SECRET_KEY,algorithms='HS256')
        ### 收集情况判断数据
        ### 从token中取出用户名user和超时时间exp
        tmp_user = decoded_jwt['user']
        tmp_exp = decoded_jwt['exp']
        ### 从数据库中取出流量trafic
        tmp_trafic = get_user_trafic(user=tmp_user)
    except:
        result['info'] = 'Token error!Please generate a new token and then use token in valid period'
        return result    
    result['user'] = tmp_user
    result['exp'] = tmp_exp
    result['trafic'] = tmp_trafic

    return result



### 请求前处理
def  request_pretreate(token_key,token):
    '''
    函数功能：

        定义一个预处理的函数

    参数：
        token_key (str): token密钥
        token (str): token字符串

    返回：
        result (dict): 结果字典
    '''

    ### 开始收集参数
    is_params = collect_params(token_key=token_key,token=token) 
    ### 根据参数收集情况进行相应处理
    ### 收集参数失败，返回错误提示信息
    if 'info' in is_params.keys():
        result = is_params
        return result
    ### 收集参数成功，开始不同情况判断
    else:
        ### 取出关键判断参数数据
        user = is_params['user']
        exp = is_params['exp']
        trafic = is_params['trafic']
        ### 获取dashare元数据信息库连接
        dashare_metadb_connection = get_dashare_metadb_connection()
        ### 使用pandas读取数据
        select_sql = "SELECT * FROM DaShareInfo"
        result_df = pd.read_sql(select_sql,con=dashare_metadb_connection)
        ### 判断用户是否存在,并将判断信息存入变量is_user
        users_list = result_df['user'].tolist()
        if str(user) in set(users_list):
            is_user = True
        else:
            is_user = False
        ### 判断token时效，并将判断信息存入变量is_exp
        now_time = time.time()
        if exp >= now_time:
            is_exp = True
        else:
            is_exp = False
        ### 获取用户流量，并将具体数值信息存入变量trafic_residual
        trafic_residual = trafic
        result = {}
        result['user'] = user
        result['is_user'] = is_user
        result['is_exp'] = is_exp
        result['trafic'] = trafic_residual

        return result



### 进行情况判断，获取数据并返回对应结果信息或数据
def get_data(pretreatment,select_sql,start_time,end_time):
    '''
    函数功能：

        定义一个根据情况，获取数据并返回对应结果信息或数据的函数

    参数：
        pretreatment (dict): 预处理信息字典
        select_sql (str): SQL查询语句
        start_time (str): 开始时间
        end_time (str): 结束时间

    返回：
        tmp_json (json): 编译后的json结果
    '''

    ### 开始预处理验证流程
    ### token验证-初始验证,应用于获取不到token的情形
    try:
        tmp_json = {'info':pretreatment['info']}
    except:
        ### token验证=进阶验证，应用于获取到token的情形
        ### 用户存在验证
        if pretreatment['is_user'] == False:
            tmp_json = {'info':'The user does not exist and may have been logged out.Please re register!'}
        else:
            ### token过时验证
            if pretreatment['is_exp'] == False:
                tmp_json = {'info':'This token is outdated,please regenerate it!'} 
            else:
                ### 根据起止时间判断需求数据量
                start_time_datetimetype = datetime.datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")
                end_time_datetimetype = datetime.datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
                time_delta = (end_time_datetimetype - start_time_datetimetype).days
                if int(pretreatment['trafic']) > int(time_delta):
                    ### 获取数据库引擎
                    ### 载入程序包中已引入，from dashare.service.dbconnection import db_engine
                    ### 查询语句编写,从dashare.service.cons中选择编写的SQL主体
                    # select_sql = """
                    # SELECT * FROM stations_xjjx.single_fanpower_data LIMIT 5
                    # """
                    ### 查询语句执行，使用pandas读取数据
                    result_df = pd.read_sql(select_sql,con=db_engine)
                    ### 查询结果转化为JSON
                    ### 数据库查询结果转化为JSON
                    result_json = result_df.to_json(orient='records',force_ascii=False)  ### 转换为字符串
                    tmp_json = json.loads(result_json)
                    ### 根据已有流量减去本次请求流量
                    residual_trafic = int(pretreatment['trafic']) - int(time_delta)
                    set_user_trafic(user=pretreatment['user'],trafic_num=residual_trafic)
                else:
                    tmp_json = {'info':"The current user's data traffic is insufficient.Please recharge before using the data service!"}      

    return tmp_json



###############################################################################################################################################################
###############################################################################################################################################################


