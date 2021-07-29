"""
算法1：base64（编码算法）
常用在URL、cookie、网页中传输少量二进制数据
"""
# 编码
import base64
byte_str = "I like you".encode("utf-8")
encode_str = base64.b64encode(byte_str)
print(encode_str)

# 解码
decode_str = base64.b64decode("SSBsaWtlIHlvdQ==")
print(decode_str.decode("utf-8"))

"""
算法2：urlencode（URL编码）
base64的特征是尾部经常带有=号
url编码的特征是%很多
"""
from urllib.parse import quote,unquote
q = '菜鸟'
# 编码
url = 'http://www.baidu.com/?text={}'.format(quote(q))
print(url)
# 解码
b = unquote('%E8%8F%9C%E9%B8%9F')
print(b)

"""
算法3：md5
md5不是编码，也不是加密，叫做摘要算法，又称哈希算法和散列算法
作用：1、防止篡改；2、校验数据
摘要算法的另一个应用场景是用来保存密码
摘要算法是不可逆的，无法解密得到原始数据
"""
import hashlib
hash = hashlib.md5()
# 明文密码是123456
hash.update(b"123456")
hash_str = hash.hexdigest()
print(hash_str)

"""
纯粹的摘要算法不是一种特别安全的方式去存储密码
可以通过”加盐“的方式提高安全性
"""
salt = 'the salt'
pwd = '8888'
salt_pwd = salt+pwd
hash = hashlib.md5()
hash.update(salt_pwd.encode("utf-8"))
hash_str = hash.hexdigest()
print(hash_str)