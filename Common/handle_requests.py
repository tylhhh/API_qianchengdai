import json,requests
from Common.handle_config import conf
from Common.handle_log import logger
def send_requests(method, url, data=None, token=None):
    logger.info("发起一次HTTP请求")
    headers = handle_header(token)
    url = pre_url(url)
    data = pre_data(data)
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))

    method = method.upper()
    if method == "GET":
        resp = requests.get(url,data, headers=headers)
    elif method == "POST":
        resp = requests.post(url, json=data, headers=headers)
    elif method == "PATCH":
        resp = requests.patch(url, json=data, headers=headers)
    logger.info("响应状态码：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))
    return resp

def handle_header(token=None):

    headers= {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type":"application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def pre_url(url):
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url

def pre_data(data):
    """
    如果data是字符串，则转换成字典对象
    :param data:
    :return:
    """
    if data is not None and isinstance(data, str):
        if data.find("null") != -1:
            data = data.replace("null","none")
        data = eval(data)
    return data






