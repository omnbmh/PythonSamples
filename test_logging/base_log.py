#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
配置一个日志的基本输出
'''

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info("start info log")
logger.debug("debug log")
logger.warn("warning log")
logger.error("log finish")
