import logging
import logging.config

# 如果不设置 level，将跟随父级的level
logger = logging.getLogger('a')
logger.info("info msg")
logger.warning("warn msg")
logger.error("error msg")

# root logger 的默认 level 是 WARN

logger_child = logging.getLogger('a.b')

# python logging 分为：
# 记录器、过滤器、处理器、格式化器
# 可以给记录器设置过滤器、处理器
# 给处理器设置过滤器、格式化器

# 日志处理逻辑为：
# logger -> level -> filter -> parent & handler
# parent: same as above
# hander -> level -> filter -> formater -> handle

# 可以通过内存配置和文件配置来配置logging，具体可餐卡config.py & config.json
logging.config.dictConfig()

#TODO: logging 的层级设置不是很理解