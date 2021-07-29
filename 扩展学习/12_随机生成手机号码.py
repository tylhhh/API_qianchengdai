"""
随机字符：random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
生成指定数量的随机字符：random.sqmple('zyxwvutsrqponmlkjihgfedcba',5)
 从a-zA-Z0-9生成指定数量的随机字符：ran_str = ''.join(random.sample(string.ascii_letters + string.digits,8))
"""

# 第一种方法
import string
import random
num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
    '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
def phone_num():
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits,8))
    res = start+end
    return res
print(phone_num())

# 第二种方法
def generator_phone():
    index = random.randint(0, len(num_start)-1)
    phone = str(num_start[index])
    for _ in range(8):
        phone += str(random.randint(0,9))
    return phone
print(generator_phone())


# 第三种方法
def mobile():
    start = random.choice(num_start)
    phone = start + ''.join(random.choice("0123456789") for _ in range(8))
    return phone
print(mobile())





