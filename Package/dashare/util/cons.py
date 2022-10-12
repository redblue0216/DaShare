# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个元数据信息库参数管理脚本，主要用于存储相应参数
"""
模块介绍
-------

这是一个元数据信息库参数管理脚本，主要用于存储相应参数

    功能：             

        （1）元数据信息库参数管理

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import yaml
import dashare as ds



####### 元数据信息库参数管理 #####################################################
### 功能：                                                                    ###
### （1）元数据信息库参数管理                                                   ###
#################################################################################



####### 元数据信息库参数管理 #############################################################################
########################################################################################################



### DASHARE_dashare_metadb_PATH：DaShare数据库路径
### 从配置文件dashare_config.yaml中获取
# DASHARE_dashare_metadb_PATH = r'D:\Workspace\JiYuan\DaShare\Demo\dashare.db'
dashare_package_path = ds.__file__.replace('__init__.py','')
dashare_config_file = open('{}dashare_config.yaml'.format(dashare_package_path),encoding='UTF-8')
dashare_config_yaml = yaml.load(dashare_config_file,Loader=yaml.FullLoader)
dashare_metadb_path = dashare_config_yaml['dashare_metadb_path']
DASHARE_METADB_PATH = r'{}'.format(dashare_metadb_path)



########################################################################################################
########################################################################################################


