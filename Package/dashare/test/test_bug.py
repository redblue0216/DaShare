from dashare.client.api import DataAPI
from functools import partial

### 设置除了token_key和token外，额外的参数
tmp_dict = {}
tmp_dict['start_time'] = '2022-05-30,00:00:00'
tmp_dict['end_time'] = '2022-06-01,00:00:00'
dashare = DataAPI(token_key = 7890,
                    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjUyMjAxMzYuMjUxNTU1LCJ1c2VyIjoidGVzdCJ9.WtRWWvvjgrhS446ZywKym5CvFUmYDN-6ut6MwxpyW4I',
                    timeout=300)
# df = dashare.query(dataapi='get_meteorological_data_local',params=tmp_dict)
df = dashare.get_meteorological_data_local(params=tmp_dict)
# print(df)
# print(type(df))
import pandas as pd
tmp_df = pd.DataFrame(df)
print(tmp_df.iloc[100:,:])
tmp_df.to_csv('test.csv')