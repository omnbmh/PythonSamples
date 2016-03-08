#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- author: c8d8z8@gmail.com

# config logging
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger.info(u'日志模块加载成功')

import commonlib.zqblib

commonlib.zqblib.login()
zqb = commonlib.zqblib.ZQB()
for i in range(1,120):
    print i
    userinfos = zqb.select_user_info(i)
    for userinfo in userinfos:
        zqb.save_user(userinfo)