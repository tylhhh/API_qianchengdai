"""
ConfigParser 是用来读取配置文件的包。
配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容
[section]
option=value

"""
# ConfigParser 初始化对象
import configparser
config = configparser.ConfigParser()
config.read("test.ini", encoding="utf-8")

# 获取所用的section节点
print(config.sections())

# 获取指定section的options
res = config.options("db")
print(res)

# 获取指定section下的指定option值
res = config.get("db", "db_host")
print(res)
# r1 = config.getint("db", "k1") #将获取到值转换为int型
# r2 = config.getboolean("db", "k2" ) #将获取到值转换为bool型
# r3 = config.getfloat("db", "k3" ) #将获取到值转换为浮点型

# 获取指定section的所用配置信息
res = config.items("db")
print(res)

# 检查section或option是否存在
if not config.has_section("default"):
    config.add_section("default")
if not config.has_option("default","db_host"):
    config.set("default","db_host","1.1.1.1")
config.write(open("test.ini","w",encoding="utf-8"))