#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################
#
# 20160926
# 配置日志
##########################################

import logging
import logging.config

def configure(configfile):
    logging.config.fileConfig(configfile)

def getLogger(loggername):
    logger = logging.getLogger(loggername)
    logger.info(u'日志模块加载成功')
