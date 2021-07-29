import logging

# 1、创建一个日志收集器
logger = logging.getLogger("mylogger")

# 2、给日志收集器设置日志级别
logger.setLevel(logging.DEBUG)

# 3、给日志收集器创建一个输出渠道
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('error.log', encoding="utf-8")
file_handler.setLevel(logging.ERROR)

# 4、给渠道设置一个日志输出内容的格式
fmt = "%(asctime)s-%(name)s-%(levelname)s：%(message)s"

# 5、将日志格式绑定到渠道当中
stream_handler.setFormatter(logging.Formatter(fmt))
file_handler.setFormatter(logging.Formatter(fmt))

# 6、将设置好的渠道添加到日志收集器上
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


