import yaml

dashare_config_file = open('D:\Workspace\JiYuan\DaShare\Demo\dashare\dashare_config.yaml',encoding='UTF-8')
dashare_config_yaml = yaml.load(dashare_config_file,Loader=yaml.FullLoader)
dashare_metadb_path = dashare_config_yaml['dashare_metadb_path']
print(dashare_config_yaml['dashare_metadb_path'])


import dashare as ds
print(ds.__file__)