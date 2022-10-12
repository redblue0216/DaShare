# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个dashare常用命令行接口类
"""
模块介绍
-------

这是一个dashare常用命令行接口类

设计模式：

    无

关键点：    

    （1）click 

主要功能：            

    （1）dashare程序管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import click
import os
import sys
from rich.console import Console
from dashare.util.info_tool import create_dashare_metadb
import dashare as ds



####### CLI命令行接口 #######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）click                                                           ###
### 主要功能：                                                            ###
### （1）dashare程序管理                                                  ###
############################################################################



###### CLI命令行接口 #####################################################################
#########################################################################################



### dashare命令组
@click.group()
@click.help_option('-H','--help')
@click.version_option('-V','--version')
def dashare():
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======                    Hello! Welcome to DaShare                ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="red")


### dashare设置环境变量
@click.command(help="set up a meta database for dashare")
def set_metadb():
    console = Console()
    result = create_dashare_metadb()
    print(result)
    console.print('=================================================================>>>>>> dashare set a meta database',style="red")


### dashare启动后台服务
@click.command(help="start atom service")
def start_service():
    console = Console()
    api_path = ds.__file__.replace('__init__.py','')### __init__.py前的atom\需要去掉，打包后
    console.print('=================================================================>>>>>> dashare servive start',style="red")
    system_platform = sys.platform
    if system_platform == 'win32':
        os.system("{} & cd {} & python .\service\main_router.py".format(api_path[:2],api_path))
    elif system_platform == 'linux':
        os.system("cd {} & python ./service/main_router.py".format(api_path))
    # uvicorn api:app --reload --host '0.0.0.0' --port 11911


### 向dashare命令组添加命令
dashare.add_command(set_metadb) 
dashare.add_command(start_service)  


### python脚本主程化
if __name__ == '__main__':
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======                    Hello! Welcome to DaShare                ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="red")
    dashare()



#################################################################################################################################################
#################################################################################################################################################


