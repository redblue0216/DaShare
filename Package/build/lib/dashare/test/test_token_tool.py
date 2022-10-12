from dashare.util.token_tool import get_user_token

tmp_token = get_user_token(user = 'test')
print(tmp_token)
a = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjUxOTM2NjUuNDI4NzMxLCJ1c2VyIjoidGVzdCJ9.upPymO1qfQhsMZ5DG9-gFzEHGgmzi6ya2diyweKlGJY'
print(a == tmp_token)