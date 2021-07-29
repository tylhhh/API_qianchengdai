
"""
json:是什么样就直接转换，没有计算,json不认单引号，json中的字符串需要用双引号包起来
eval:python表达式去计算
"""
import json
ss = '{"mobile_phone":"18600001112","pwd":"123456789","type":1,"reg_name":"美丽可爱的小简","flag":null}'

# json字符串转换成字典
ss_dict = json.loads(ss)
print(ss_dict)
print(type(ss_dict))

dict_ss = {'mobile_phone': '18600001112', 'pwd': '123456789', 'type': 1, 'reg_name': '小可爱', 'flag': None}
# 将字典转换成json字符串
ss_json = json.dumps(dict_ss, ensure_ascii=False)
print(ss_json)
print(type(ss_json))

if ss.find("null") != -1:
    ss = ss.replace("null", "None")

s = eval(ss)
print(s)
print(type(s))

# 遇到特殊类型的时候，eval通常用了执行一个字符串表达式，并返回表达式的值
print(eval('1+1'))
# print(json.loads("1+1"))