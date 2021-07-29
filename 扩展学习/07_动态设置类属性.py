"""
反射：指通过“字符串”对 对象的属性和方法进行操作(查找/获取/删除/添加)
反射常常用在动态加载的模块中
hasattr：通过“字符串”判断对象的属性或方法是否存在
getattr：通过“字符串”获取对象的属性或方法
setattr：通过“字符串”设置对象的属性或方法
delattr：通过“字符串”删除对象的属性或方法
"""

class AAA:
    name = "小明"
    pass

s = AAA()
setattr(s, "age", 18)
setattr(s, "name", "哈哈哈")
setattr(AAA,"age", 20)
print(getattr(s, "age"))
print(hasattr(s, "age"))
# delattr(s, "age")
# print(hasattr(s, "age"))
print(AAA.__dict__) # 打印类中的属性有哪些
print(s.__dict__)  # 打印实例化对象的属性有哪些
print(AAA.age)

# 清理类属性
values = dict(AAA.__dict__)
for key,value in values.items():
    if key.startswith("__"):
        pass
    else:
        delattr(AAA, key)
print(AAA.__dict__)


# 清理对象属性
values = dict(s.__dict__)
for key,value in values.items():
    delattr(s, key)
print(s.__dict__)





