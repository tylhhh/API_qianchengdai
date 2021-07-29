"""
re 模块使 Python 语言拥有全部的正则表达式功能。
re.findall(re规则，字符串)：把所有匹配的字符放在列表中并返回
re.sub(re规则，替换串，被替换串)：匹配字符并替换
"""

"""
${memberID} 对应的正则表达式 '\$\{.*\}'
\$ 转义替换字符串中 $
\{ 转义替换字符串中 {
. 除了\n中的任意单个自符
* 匹配*前面的字符零次或者多次
\} 转义替换字符串中 }
"""
import re

dict = {"memberId": "${memberID}", "password": "123456", "loanId": "${loanId}", "amount": "-100"}
data = {"memberId": 10001, "loanId": 1}
for key, value in dict.items():
    if key in data.keys():
        newValue = re.sub('\$\{.*\}', str(data[key]), value)
        dict[key] = newValue
print(dict)


class EnvData:
    pass


setattr(EnvData, "member_id", "12345678900000")
setattr(EnvData, "user_money", "2500")
# 利用re.findall(re规则，字符串)
data = '{"member_id": #member_id#,"amount":600,money:#user_money#,username:"#user#"}'
res = re.findall("#(.*?)#", data)  # 如果没找到，则返回的是一个空列表
print(res)
if res:
    for item in res:
        try:
            value = getattr(EnvData, item)
            data = data.replace("#{}#".format(item), value)
        except AttributeError:
            continue
print(data)

# 利用re.sub(re规则，替换串，被替换串)，缺点：key-value的名称要对应
data1 = '{"member_id": "#member_id#","amount":600,"user_money":"#user_money#","username":"#user#"}'
dict_data = eval(data1)
for key, value in dict_data.items():
    if hasattr(EnvData, key):
        value1 = getattr(EnvData, key)
        newValue = re.sub("#(.*)#", value1, value)
        dict_data[key] = newValue
print(dict_data)
