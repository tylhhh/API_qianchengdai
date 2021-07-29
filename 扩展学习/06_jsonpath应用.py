"""
文章地址：
http://www.lemfix.com/topics/63
安装：pip install jsonpath
使用方式：jsonpath.jsonpath(字典对象,jsonpath表达式)
返回值：列表。

jsonpath用来解析多层嵌套的json数据
使用方法如下：
import jsonpath
res = jsonpath.jsonpath(dic_name,'$..key_name')
嵌套n层也能取到所有key_name信息，其中“$”表示最外层{}，“..”表示模块匹配，当不传入不存在的key_name时，程序会返回false
"""

import jsonpath
d={
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2059,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18378309272",
                        "gold": 10896,
                        "info":{
                            "card":434345432,
                            "bank_name":'中国银行'
                        }

                },
                {
                        "id": 2067,
                        "name": "小黑",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "12345678915",
                        "gold": 100
                }
        ]
}
res = jsonpath.jsonpath(d, "$..name")  # $表示最外层的{}，获取所有学生姓名，存放在列表中
print(res)
a = jsonpath.jsonpath(d, "$..name")[0]
print(a)
res1 = jsonpath.jsonpath(d, "$.stu_info.[0].info.bank_name")
print(res1)
