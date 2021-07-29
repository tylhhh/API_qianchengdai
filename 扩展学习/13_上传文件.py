"""
requests模块传参有四种方式：params、data、json和files
params：传递查询字符串参数（常用于get请求）
data：传递表单类型的参数（参数类型：Content-Type:application/x-www-form-urlencoded）
json：传递json类型的参数（参数类型：Content-Type:application/json）
files：用于上传文件（参数类型： content-type:multipart/form-data）
files为字典类型，上传的文件为键值对的形式，参数名作为键
参数值是一个元组，内容为一下格式（文件名，打开的文件流，文件类型）
注意：除了上传的文件，接口其他参数不能放入files中
系统为请求头设置了正确边界，边界是被自动加到请求头的，所以我们不用再自己定义Content-Type请求头设置
"""
import requests
def uploadImages(file_path,filename):
    url="http://elm.cangdu.org/v1/addimg/food"
    headers = {"Content-Type":"multipart/form-data"}
    # 上传的文件参数
    data = {"file":(filename,open(file_path,"rb"),'image/jpeg')}
    res = requests.post(url=url,files=data)
    print(res.json())


if __name__ == '__main__':
    case = {"file_path": "E:\Downloads\日本1.png","filename":"真龙霸业.png"}
    uploadImages(case["file_path"],case["filename"])

# data={"file":("真龙霸业.png",open("E:\Downloads\日本1.png","rb"),'image/jpeg')}





