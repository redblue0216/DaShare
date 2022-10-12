import hashlib



password = '123456'
SALT = 'dashare'
md5_salt = hashlib.md5((password + SALT).encode('utf-8'))
md5_salt_password = md5_salt.hexdigest()
print(md5_salt_password == 'ef721078b766b4da0245e5c985f84476')



