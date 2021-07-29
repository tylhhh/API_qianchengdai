import requests
# url = "http://api.lemonban.com/futureloan/member/login"
# data = {"mobile_phone":"18600001112","pwd":"123456789"}
# headers = {"X-Lemonban-Media-Type": "lemonban.v2","Content-Type":"application/json"}
# resp = requests.post(url, json=data, headers=headers)
# # 响应状态码
# print(resp.status_code)
# # 响应头
# print(resp.headers)
# # 响应体
# print(resp.json())

"""
requests实现cookies鉴权
方法一：创建一个会话对象，自动去获取
"""
print("\n************************************requests实现cookies鉴权，方法一**********************************************")
# 实例化Session（）对象
s = requests.Session()
# 登录，获取cookies鉴权，即cookies的值
login_url = "https://v4.ketangpai.com/UserApi/login"
login_data = {"email": "2441413919@qq.com", "password": "a1b2c3d4",  "remember": 0}
s.post(login_url, data=login_data)  # 主动将响应中的set-cookies添加到对象中
print("登录之后的cookies：",s.cookies)
# 获取用户信息
user_url = "https://v4.ketangpai.com/UserApi/getUserInfo"
resp = s.get(user_url)
print(resp.json())


"""
requests实现cookies鉴权
方法二：需要自己主动获取cookies，并在后续的请求中，主动加上cookies
"""
print("\n************************************requests实现cookies鉴权，方法二**********************************************")
login_url = "https://v4.ketangpai.com/UserApi/login"
login_data = {"email": "2441413919@qq.com", "password": "a1b2c3d4",  "remember": 0}
resp = requests.post(url=login_url,data=login_data)
print(resp.json())
# 主动获取cookies
cookies = resp.cookies
print("主动获取的cookies:",cookies)
# 获取用户信息
user_url = "https://v4.ketangpai.com/UserApi/getUserInfo"
resp = requests.get(user_url,cookies=cookies)
print(resp.json())




"""
requests实现token鉴权
"""
print("\n************************************requests实现token鉴权**********************************************")
# 登录，获取token
login = "http://api.lemonban.com/futureloan/member/login"
login_datas = {"mobile_phone":"18678451245","pwd":"123456789"}
headers = {"X-Lemonban-Media-Type": "lemonban.v2","Content-Type":"application/json"}
resp = requests.post(login, json=login_datas, headers=headers)
print(resp.json())
# 在响应中获取token的值
token = resp.json()["data"]["token_info"]["token"]
# 在响应中获取member_id的值
member_id = resp.json()["data"]["id"]
print(token)

# 充值，将token添加到请求头当中
headers["Authorization"] = "Bearer {}".format(token)

"""
客服系统后台登录鉴权
"""
print("\n************************************客服系统后台登录鉴权**********************************************")
dandian_login_url="https://passport.ijunhai.com/auth/login"
dandian_login_data ={"username":"tangyuling002","password":"u06ivJGV","redirect_url":"https://cshw-test.ijunhai.com/login","application_id":21}
headers = {"Content-Type":"application/json"}
resp = requests.post(url=dandian_login_url,json=dandian_login_data,headers=headers)
print(resp.json())
# 1、获取单点系统授权的code
code = resp.json()["content"]["code"]
kefu_login_url="https://cshw-test.ijunhai.com/api/login"
kefu_login_data = {"code":code}
resp = requests.post(url=kefu_login_url,json=kefu_login_data,headers=headers)
# 2、获取客服后台登录后的token值
token = resp.json()["token"]
# 3、将token添加到请求头当中
headers["authorization"] = "Bearer {}".format(token)
# 例如获取个人信息
get_me_url = "https://cshw-test.ijunhai.com/api/admin/staff/me"
resp = requests.get(url=get_me_url,headers=headers)
print(resp.json())


"""
少女心后台登录鉴权,token值就是单点登录后的code值，放在请求参数中
"""
print("\n************************************少女心后台登录鉴权**********************************************")
dandian_login_url="https://passport.ijunhai.com/auth/login"
dandian_login_data ={"username":"tangyuling002","password":"u06ivJGV","redirect_url":"http://mkt.itrigirls.com:8090/ad-system.html","application_id":21}
headers = {"Content-Type":"application/json"}
resp = requests.post(url=dandian_login_url,json=dandian_login_data,headers=headers)
print(resp.json())
# 1、获取单点系统授权的code
code = resp.json()["content"]["code"]
itrigirls_login_url="http://mkt.itrigirls.com:8090/v1/login"
itrigirls_login_data = {"auth_code":code}
resp = requests.get(url=itrigirls_login_url,params=itrigirls_login_data)
print(resp.json())
# 将auth_code值添加到请求参数中，例如获取素材数据
material_url = "http://mkt.itrigirls.com:8090/v1/material/getFile"
material_data = {"pid":"","per_page":100,"page":1,"search":"","material_type":[],"material_size":[],"material_format":[],"creator":[],"date":[],"order_field":"created_at","order_type":"desc","tag_ids":[],"auth_token":code}
resp = requests.post(url=material_url,json=material_data)
print(resp.json())







