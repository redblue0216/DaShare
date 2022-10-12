# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个DaShare服务应用主路由类，主要使用fastapi搭建ASGI服务器
"""
模块介绍
-------

这是一个DaShare服务应用主路由类，主要使用fastapi搭建ASGI服务器

设计模式：

    无

关键点：    

    （1）fastapi

主要功能：            

    （1）DaShare服务应用主路由
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from fastapi import FastAPI
import uvicorn
from dashare.service.user_router import user_router
from dashare.service.meteorological_router import meteorological_router
from dashare.service.wind_turbine_router import wind_turbine_router



####### DaShare服务应用主路由 ###############################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）fastapi                                                          ###
### 主要功能：                                                            ###
### （1）DaShare服务应用                                                  ###
############################################################################



###### DaShare服务应用主路由操作 #####################################################################
####################################################################################################



### 创建fastapi应用实例
app = FastAPI()
app.include_router(user_router,prefix="/user",tags=['user'])
app.include_router(meteorological_router,prefix="/meteorological",tags=['meteorological'])
app.include_router(wind_turbine_router,prefix="/wind_turbine",tags=['wind_turbine'])



if __name__ == '__main__':
    uvicorn.run(app='main_router:app',host='0.0.0.0',port=11911,reload=True,debug=True) ### app参数需要使用字符串格式的时候，才可以添加reload和debug参数



####################################################################################################
####################################################################################################


