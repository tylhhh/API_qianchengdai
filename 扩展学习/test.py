
import hashlib
def md5(str):
    str_md5 = hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()
    return str_md5

def get_mol_sign(request_data):
    str_parm = ''  # 目标md5串
    data_dict = eval(request_data)
    list_data = sorted(data_dict)
    for item in list_data:  # 将字典中的key排序,存在在列表中
        if item == "signature":
            list_data.remove("signature")
    for item in list_data:  # 列表去掉signature后，再进行遍历,拼接参数字典中的value值
        str_parm = str_parm + str(data_dict[item])
    secret_key = '6HHT8uQ3V0ZK8ozmvedeTY9uhDaXUsNv'  # mol回调固定的
    str_parm = str_parm + secret_key
    print(str_parm)
    signature = md5(str_parm)
    print(signature)
    return signature



if __name__ == '__main__':
    request_data = ""