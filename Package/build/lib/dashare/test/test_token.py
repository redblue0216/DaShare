import jwt 
import time

# # 加密密钥 这个很重要千万不能泄露了
# SECRET_KEY = "123456"
 
# # 设置过期时间 现在时间 + 有效时间    示例5分钟
# expire = time.time() + 60 * 5
# print(expire)
 
# # exp 是固定写法必须得传  sub和uid是自己存的值
# to_encode = {"exp": expire, "sub": str(123456), "uid": "12345"}
 
# # 生成token 
# encoded_jwt = jwt.encode(payload = to_encode,key = SECRET_KEY,algorithm = "HS256")
# print(encoded_jwt)
encoded_jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjUyMDQ4NzYuMzY5Nzc4OSwidXNlciI6InRlc3QifQ.u4FJs6nsby3wmKn7WuxNozhMccIdgGrceCjpGkUsFFk'
SECRET_KEY = '7890'
# 解码
decoded_jwt = jwt.decode(jwt = encoded_jwt,key = SECRET_KEY,algorithms = "HS256")
print(type(decoded_jwt),decoded_jwt)
exp = decoded_jwt['exp']
print(exp)
print(time.time())
print('----')