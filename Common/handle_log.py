import logging,os
from Common.handle_config import conf
from Common.handle_path import logs_dir
class HandleLog:

    def __init__(self,name, path):
        # 创建一个日志收集器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.stream_handle = logging.StreamHandler()
        self.file_handle = logging.FileHandler(path, encoding="utf-8")
        fmt = ' %(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)dline-日志信息: %(message)s '
        self.stream_handle.setFormatter(logging.Formatter(fmt))
        self.file_handle.setFormatter(logging.Formatter(fmt))
        self.logger.addHandler(self.stream_handle)
        self.logger.addHandler(self.file_handle)

    def get_logger(self):
        return self.logger

    def __del__(self):
        self.logger.removeHandler(self.stream_handle)
        self.logger.removeHandler(self.file_handle)
        self.stream_handle.close()
        self.file_handle.close()

if conf.getboolean("log", "file_ok"):
    file_path = os.path.join(logs_dir, conf.get("log", "file_name"))
else:
    file_path = None

mlogger = HandleLog(conf.get("log", "name"),file_path)
logger = mlogger.get_logger()
logger.info("测试日志")