# logging 可以通过配置方式，方便的配置记录器以及相关的处理器和过滤器
import logging
import logging.config
import sys
import json
cfg = {
    'version': 1, # version 必须存在 且 值只能为1
    'incremental': False,
    # formatters
    'formatters': {
        # 关键字 与 logging.Formatter初始化关键字保持一致
        # class logging.Formatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None)
        'format1': {
            'format': '%(asctime)s %(filename)s %(funcName)s  %(lineno)s %(levelname)s %(message)s', # 可参考 https://docs.python.org/3.7/library/logging.html#logrecord-attributes
            'datefmt': '%Y-%m-%d %H:%M:%S',
            # 默认使用logging.Formatter，当然我们可以自定义，解释器根据name以及__import__方法寻找对应类
            'class': 'logging.Formatter'
        }
    },
    'filters': {
        'filter1': {
            # 关键字 与 logging.Filter 保持一致
            'name': ''
        }
    },
    'handlers': {
        'handler1': {
            'formatter': 'format1',
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            # 指定其他参数来初始化logging.FileHandler 与 类的初始化保持一致
            'filename': 'log.txt'
        },
        'handler2': {
            'formatter': 'format1',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stderr
        }
    },
    'loggers': {
        'logger1': {
            'handlers': ['handler1', 'handler2'],
            'level': 'DEBUG',
            'filter': 'filter1'
        }
    }
}

# 从字典读取配置
# try:
#     logging.config.dictConfig(cfg)
# except Exception as e:
#     print(e)
# logger = logging.getLogger('logger1')
# logger.info('This is info message')

# 从文件读取配置
with open('config.json') as fp:
    fCfg = json.load(fp)

logging.config.dictConfig(fCfg)
logger = logging.getLogger('logger1')
logger.info('This is info message')