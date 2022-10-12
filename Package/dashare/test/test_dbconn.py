from dashare.service.dbconnection import db_engine
import pandas as pd

sql = """
SELECT * FROM stations_xjjx.single_fanpower_data LIMIT 5
"""
result_df = pd.read_sql(sql,con=db_engine)
print(result_df,type(result_df))