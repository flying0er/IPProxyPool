#!/usr/bin/env python
# coding: utf-8

"""log_conf.py
日志输出配置

renyuxiong 2017.06.11 09:39
"""

from conf.proxy_conf import DEBUG

CONF = {}

CONF["log_dir"] =  "/tmp/" if DEBUG else "/mnt/logs/"
CONF["log_level"] = "debug" if DEBUG else "warn" # info error critical
