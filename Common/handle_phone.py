import random
from Common.handle_db import HandleDB
from Common.handle_requests import send_requests
from Common.handle_config import conf
prefix = [133, 149, 153, 173, 177, 180, 181, 189, 199,
          130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 166,
          134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198
          ]

def user_phone():

    index = random.randint(0, len(prefix)-1)
    phone = str(prefix[index])
    for _ in range(0,8):
        phone += str(random.randint(0,9))  # 转换成字符串才能直接拼接
    return phone


def get_new_phone():
    db = HandleDB()
    while True:
        phone = user_phone()
        sql = 'select * from member where mobile_phone="{}"'.format(phone)
        count = db.get_count(sql)
        if count == 0:
            db.close()
            return phone


def get_old_phone():
    user = conf.get("general_user","user")
    passwd = conf.get("general_user","passwd")
    send_requests("POST","member/register",{"mobile_phone":user,"pwd":passwd})
    return user,passwd







