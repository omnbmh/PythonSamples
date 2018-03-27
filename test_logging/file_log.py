#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 设置 handler
handler = logging.FileHandler("log/file_log.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# logging 设置完成

logger.info("file info log")
logger.debug("file debug log")
logger.warn("file warn log")
logger.error("file error log")


