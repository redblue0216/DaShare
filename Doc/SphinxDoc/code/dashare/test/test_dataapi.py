
from dashare.client.api import DataAPI
from functools import partial

### 设置除了token_key和token外，额外的参数
tmp_dict = {}
tmp_dict['entity'] = 'XJJX'
tmp_dict['start_time'] = '2022-05-30,00:00:00'
tmp_dict['end_time'] = '2022-06-01,00:00:00'
dashare = DataAPI(token_key = 7890,
                    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjU0NjkxMTQuMTI4MDg4LCJ1c2VyIjoidGVzdCJ9.HgmyjDabinqOxU9v7DaKsPraFZd948SMfA9HGhTg-7U',
                    timeout=6000)
# df = dashare.query(dataapi='get_meteorological_data_local',params=tmp_dict)
# df = dashare.get_wind_nwp_data_updated_local(params=tmp_dict)
# df = dashare.get_wind_nwp_data_history_local(params=tmp_dict)
# df = dashare.get_wind_measure_data_local(params=tmp_dict)
df = dashare.get_wind_turbine_data_local(params=tmp_dict)
print(df)







