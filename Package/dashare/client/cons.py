# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个客户端参数管理脚本，主要用于存储相应参数
"""
模块介绍
-------

这是一个客户端参数管理脚本，主要用于存储相应参数

    功能：             

        （1）客户端参数管理

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################






####### 客户端参数管理 ##########################################################
### 功能：                                                                   ###
### （1）客户端参数管理                                                       ###
################################################################################



####### 客户端参数管理 ##################################################################################
########################################################################################################



### 基础组件参数管理，为所有数据服务接口的基础
REQUEST_PROTOCOL = {'http':'http'}
REQUEST_HOST = {'local':'127.0.0.1'}
REQUEST_PORT = {'default':'8000'}
DATAAPI = {'meteorological':'meteorological',
            'wind_turbine':'wind_turbine'}
OPERATOR = {'get_wind_nwp_data_updated':'get_wind_nwp_data_updated',
            'get_wind_nwp_data_history':'get_wind_nwp_data_history',
            'get_wind_measure_data':'get_wind_measure_data',
            'get_wind_turbine_data':'get_wind_turbine_data'}



### 具体接口路由管理，由基础组件拼接而成
### 本地气象NWP更新数据路由
GET_WIND_NWP_DATA_UPDATED_LOCAL = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['local'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['meteorological'] + \
                                '/' + OPERATOR['get_wind_nwp_data_updated'] + \
                                '?'
### 本地气象NWP历史数据路由
GET_WIND_NWP_DATA_HISTORY_LOCAL = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['local'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['meteorological'] + \
                                '/' + OPERATOR['get_wind_nwp_data_history'] + \
                                '?'         
### 本地气象实测数据路由
GET_WIND_MEASURE_DATA_LOCAL = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['local'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['meteorological'] + \
                                '/' + OPERATOR['get_wind_measure_data'] + \
                                '?'
### 本地风机数据路由
GET_WIND_TURBINE_DATA_LOCAL = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['local'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['wind_turbine'] + \
                                '/' + OPERATOR['get_wind_turbine_data'] + \
                                '?'                                                                                       



### 具体接口路由汇集管理,用于api脚本实现if-elif的flat条件判断功能，避免大量条件语句，提高代码可读性
API_DICT = {}
### 本地气象NWP更新数据路由
API_DICT['get_wind_nwp_data_updated_local'] = GET_WIND_NWP_DATA_UPDATED_LOCAL
### 本地气象NWP历史数据路由
API_DICT['get_wind_nwp_data_history_local'] = GET_WIND_NWP_DATA_HISTORY_LOCAL
### 本地气象实测数据路由
API_DICT['get_wind_measure_data_local'] = GET_WIND_MEASURE_DATA_LOCAL
### 本地风机数据路由
API_DICT['get_wind_turbine_data_local'] = GET_WIND_TURBINE_DATA_LOCAL



##############################################################################################
##############################################################################################


