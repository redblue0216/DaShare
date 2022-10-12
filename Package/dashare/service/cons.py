# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个服务端参数管理脚本，主要用于存储相应参数和SQL查询语句
"""
模块介绍
-------

这是一个服务端参数管理脚本，主要用于存储相应参数和SQL查询语句

    功能：             

        （1）服务端参数管理和SQL查询语句管理

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################






####### 服务端参数管理 ###########################################################
### 功能：                                                                    ###
### （1）服务端参数管理和SQL查询语句管理                                         ###
#################################################################################



####### 服务端参数管理 ##################################################################################
########################################################################################################



### dialect：数据库类型
SERVICE_DIALECT = 'mysql'
### driver：数据库驱动选择
SERVICE_DRIVER = 'pymysql'
### username：数据库用户名
SERVICE_USERNAME = 'root'
### password： 用户密码
SERVICE_PASSWORD = 'Passw0rd!'
### host：服务器地址
SERVICE_HOST = '39.104.77.195'
### port：端口
SERVICE_PORT = '3306'
### database：数据库
SERVICE_DATABASE = 'stations_xjjx'



####### 数据库查询语句整理 ##################################################################################
###########################################################################################################



### db:stattion_xjjx数据库对应查询语句
### table:forecast_wind_data
STATION_XJJX_FORECAST_WIND_DATA = "SELECT \
                                    `id`, \
                                    `date_time`, \
                                    `date`, \
                                    `hour`, \
                                    `minute`, \
                                    `temp`, \
                                    `radi`, \
                                    `ugrd`, \
                                    `vgrd`, \
                                    `air_presure`, \
                                    `humi`, \
                                    `total_flux`, \
                                    `visible_flux`, \
                                    `diffuse_flux`, \
                                    `direct_flux`, \
                                    `wind_speed`, \
                                    `wind_dire`, \
                                    `temp80`, \
                                    `wspeed80`, \
                                    `wspeed100`, \
                                    `wdirect80`, \
                                    `wdirect100`, \
                                    `temp1`, \
                                    `temp2`, \
                                    `temp3`, \
                                    `temp4`, \
                                    `temp5`, \
                                    `temp6`, \
                                    `extras`, \
                                    `version_num`, \
                                    `cal_time`, \
                                    `create_time`, \
                                    `update_time`, \
                                    `upload_flag` \
                                    FROM stations_xjjx.forecast_wind_data WHERE date_time BETWEEN '{start_time}' AND '{end_time}'"


### table:forecast_wind_data_history
STATION_XJJX_FORECAST_WIND_DATA_HISTORY = "SELECT \
                                            `id`, \
                                            `date_time`, \
                                            `temp`, \
                                            `radi`, \
                                            `ugrd`, \
                                            `vgrd`, \
                                            `air_presure`, \
                                            `humi`, \
                                            `total_flux`, \
                                            `visible_flux`, \
                                            `diffuse_flux`, \
                                            `direct_flux`, \
                                            `wind_speed`, \
                                            `wind_dire`, \
                                            `temp80`, \
                                            `wspeed80`, \
                                            `wspeed100`, \
                                            `wdirect80`, \
                                            `wdirect100`, \
                                            `temp1`, \
                                            `temp2`, \
                                            `temp3`, \
                                            `temp4`, \
                                            `temp5`, \
                                            `temp6`, \
                                            `extras`, \
                                            `version_num`, \
                                            `cal_time`, \
                                            `create_time` \
                                            FROM stations_xjjx.forecast_wind_data_history WHERE date_time BETWEEN '{start_time}' AND '{end_time}'"                                


### table:weather_data
STATION_XJJX_WEATHER_DATA = "SELECT \
                                `id`, \
                                `date_time`, \
                                `radi_day_accum1`, \
                                `radi_day_accum2`, \
                                `temp1`, \
                                `temp2`, \
                                `temp3`, \
                                `temp4`, \
                                `temp5`, \
                                `temp80`, \
                                `env_temp`, \
                                `env_humi`, \
                                `dew_temp`, \
                                `pressure`, \
                                `altitude`, \
                                `wind_inst`, \
                                `wind2`, \
                                `wind10`, \
                                `wspeed10`, \
                                `wspeed30`, \
                                `wspeed50`, \
                                `wspeed70`, \
                                `wspeed80`, \
                                `wspeed90`, \
                                `wspeed100`, \
                                `wspeed_hubheight`, \
                                `wdirect10`, \
                                `wdirect30`, \
                                `wdirect50`, \
                                `wdirect70`, \
                                `wdirect80`, \
                                `wdirect90`, \
                                `wdirect100`, \
                                `wdirect_hubheight`, \
                                `temp10`, \
                                `humi10`, \
                                `pressure10`, \
                                `wind_dire`, \
                                `radi_inst1`, \
                                `radi_inst2`, \
                                `radi_inst3`, \
                                `rain`, \
                                `sun_inst`, \
                                `elec`, \
                                `sun_time`, \
                                `send_flag`, \
                                `create_time`, \
                                `weather_device` \
                                FROM stations_xjjx.weather_data WHERE date_time BETWEEN '{start_time}' AND '{end_time}'"


### table:single_fanpower_data
STATION_XJJX_SINGLE_FANPOWER_DATA = "SELECT \
                                        `id`, \
                                        `name`, \
                                        `fan_type`, \
                                        `lat`, \
                                        `lng`, \
                                        `general_status`, \
                                        `state`, \
                                        `date_time`, \
                                        `active_power`, \
                                        `reactive_power`, \
                                        `real_wspeed`, \
                                        `real_wdirect`, \
                                        `rotational_speed`, \
                                        `pitch_angle1`, \
                                        `pitch_angle2`, \
                                        `pitch_angle3`, \
                                        `temp`, \
                                        `power_sign`, \
                                        `real_active_power`, \
                                        `reserve1`, \
                                        `reserve2`, \
                                        `reserve3`, \
                                        `reserve4`, \
                                        `reserve5`, \
                                        `reserve6`, \
                                        `reserve7`, \
                                        `reserve8`, \
                                        `reserve9`, \
                                        `reserve10`, \
                                        `wspeed10`, \
                                        `fault_state`, \
                                        `limit_power_state`, \
                                        `state1`, \
                                        `state2`, \
                                        `state3`, \
                                        `state4`, \
                                        `state5`, \
                                        `state6`, \
                                        `state7`, \
                                        `state8`, \
                                        `state9`, \
                                        `state10`, \
                                        `capacity`, \
                                        `is_sample`, \
                                        `create_time`, \
                                        `update_time` \
                                        FROM stations_xjjx.single_fanpower_data WHERE date_time BETWEEN '{start_time}' AND '{end_time}'"



####### 数据查询语句整理字典 #################################################################################################################
############################################################################################################################################



### 将具体业务场景数据查询汇集到一个字典中方便数据服务路由调用，避免写多个条件判断
### 气象NWP更新数据查询语句
METEOROLOGICAL_WIND_NWP_UPDATED_DATA_DICT = {}
METEOROLOGICAL_WIND_NWP_UPDATED_DATA_DICT['XJJX'] = STATION_XJJX_FORECAST_WIND_DATA
### 气象NWP历史数据查询语句
METEOROLOGICAL_WIND_NWP_HISTORY_DATA_DICT = {}
METEOROLOGICAL_WIND_NWP_HISTORY_DATA_DICT['XJJX'] = STATION_XJJX_FORECAST_WIND_DATA_HISTORY
### 气象实测数据查询语句
METEOROLOGICAL_WIND_MEASURE_DATA_DICT = {}
METEOROLOGICAL_WIND_MEASURE_DATA_DICT['XJJX'] = STATION_XJJX_WEATHER_DATA
### 风机数据查询语句
WIND_TURBINE_DATA_DICT = {}
WIND_TURBINE_DATA_DICT['XJJX'] = STATION_XJJX_SINGLE_FANPOWER_DATA



############################################################################################################################################
############################################################################################################################################


