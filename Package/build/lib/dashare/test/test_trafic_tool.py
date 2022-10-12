from dashare.util.trafic_tool import get_user_trafic,set_user_trafic

tmp_trafic = get_user_trafic('test')
print(tmp_trafic)
tmp_result = set_user_trafic(user='test',trafic_num=100)
print(tmp_result)