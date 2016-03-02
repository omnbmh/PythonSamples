#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- author: c8d8z8@gmail.com

# config logging
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger.info('日志模块加载成功')

import commonlib.zqblib

commonlib.zqblib.login()
zqb = commonlib.zqblib.ZQB()
zqb.select_user_info()