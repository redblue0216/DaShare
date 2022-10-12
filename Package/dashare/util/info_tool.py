# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个信息工具类，主要功能创建元数据库，主要技术sqlite3
"""
模块介绍
-------

这是一个信息工具类，主要功能创建元数据信息库，主要技术sqlite3

    功能：             

        （1）元数据信息库创建

类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from dashare.util import cons as ct
import sqlite3
import hashlib
import dashare as ds



####### 信息工具类 ###############################################################
### 功能：                                                                    ###
### （1）元数据信息库创建                                                       ###
#################################################################################



####### 信息工具类 ######################################################################################
########################################################################################################



### 创建dashare元数据信息库
def create_dashare_metadb(dashare_metadb_path = ct.DASHARE_METADB_PATH,*args,**kwargs):
    '''
    函数功能：

        定义一个创建dashare元数据信息库的函数

    参数：
        dashare_metadb_path (str): dashare元数据信息库路径

    返回：
        result (str): 创建成功结果信息
    '''

    ### 获取包安装后的路径site-packages/dashare/
    dashare_metadb_path_in_pkg = ds.__file__.replace('__init__.py','') 
    ### 开始创建数据库
    dashare_metadb_connection = sqlite3.connect(dashare_metadb_path_in_pkg + dashare_metadb_path)
    dashare_metadb_cursor = dashare_metadb_connection.cursor()
    dashare_metadb_cursor.execute('''CREATE TABLE IF NOT EXISTS DaShareInfo(
        user TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL,
        trafic TEXT NOT NULL 
    )
    ''')
    dashare_metadb_cursor.close()
    dashare_metadb_connection.close()
    result = 'DaShare metadb create well done!====>>{}'.format(dashare_metadb_path)
    print(result)

    return result



### 获取dashare元数据信息库操作游标
def get_dashare_metadb_connection(dashare_metadb_path = ct.DASHARE_METADB_PATH,*args,**kwargs):
    '''
    函数功能：

        定义一个获取dashare元数据信息库操作游标的函数

    参数：
        dashare_metadb_path (str): dashare元数据信息库路径

    返回：
        dashare_metadb_connection (obj): dashare元数据信息库连接
    '''


    dashare_metadb_connection = sqlite3.connect(dashare_metadb_path)

    return dashare_metadb_connection



### 加密密码
def encrypt_password(password,salt='dashare',algorithm='md5'):
    '''
    函数功能：

        定义一个加密密码的函数，默认使用md5加密算法

    参数：
        password (str): 密码
        salt (str): 密码加盐，默认为dashare
        algorithm (str): 加密算法

    返回：
        encrypted_pwd (str): 加密后的密码
    '''

    SALT = salt
    md5_salt = hashlib.md5((password + SALT).encode('utf-8'))
    encrypted_pwd = md5_salt.hexdigest()

    return encrypted_pwd



#############################################################################################################
#############################################################################################################


