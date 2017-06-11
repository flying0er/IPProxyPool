#!/usr/bin/env python
# coding: utf-8


'''Logger.py
日志输出工具

Mr.0  2017.06.11 09:34
'''

import os
import logging
import logging.handlers
import traceback

from conf.log_conf import CONF as LOG_CONF

# 日志文件路径
LOG_DIR_PATH = LOG_CONF["logger_dir"]
# 日志文件大小(兆)
LOG_FILE_MEGA_SIZE = 10
# 日志文件留存数量
LOG_FILE_BAK_COUNT = 10
# 保证logger初始化一次
ALL_LOGGERS = {}


def StandardHandler(base_name, log_dir):
    '''日志处理器
    :param  base_name  日志文件名
    :parma  log_dir    日志目录
    '''

    log_file_path = os.path.join(log_dir, base_name + '.log')

    handler = logging.handlers.RotatingFileHandler(
        filename=log_file_path,
        mode='a',
        maxBytes= LOG_FILE_MEGA_SIZE * 1024 * 1024,
        backupCount= LOG_FILE_BAK_COUNT,
        encoding='utf8'
    )

    return handler


def StandardFormatter():
    '''日志格式化工具
    '''

    format="%(asctime)s %(levelname)s -- %(filename)s in function " \
        "%(funcName)s, at line %(lineno)d, %(message)s"
    formatter = logging.Formatter(format)

    return formatter


def GetLogger(logger_name, log_dir=LOG_DIR_PATH ):

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except Exception, e:
            print traceback.format_exc()
            return False

    # getLogger不指定名称,避免logger继承,导致消息重复传播
    logger = logging.getLogger()
    logger.propagate = 0
    handler = StandardHandler(logger_name, log_dir)
    formatter = StandardFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 此处设置日志输出级别
    if LOG_CONF["log_level"] == "debug":
        logger.setLevel(logging.DEBUG)
    elif LOG_CONF["log_level"] == "info":
        logger.setLevel(logging.INFO)
    elif LOG_CONF["log_level"] == "warn":
        logger.setLevel(logging.WARN)
    elif LOG_CONF["log_level"] == "error":
        logger.setLevel(logging.ERROR)
    elif LOG_CONF["log_level"] == "critical":
        logger.setLevel(logging.CRITICAL)
    else:
        logger.setLevel(logging.DEBUG)

    return logger


def test():

    logger = GetLogger('test')

    # 日志的五种级别
    for i in range(0,10):
        logger.debug('debugdegbugdebug')
        logger.info('123qweqwsd')
        logger.warn('warnwarnwarn')
        logger.error('errorewrrorerror')
        logger.critical('criticalcritical')




if __name__ == '__main__':

    test()

