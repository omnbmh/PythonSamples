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
import commonlib.capturedatalib
import commonlib.pathlib

commonlib.zqblib.login()
zqb = commonlib.zqblib.ZQB()

#commonlib.capturedatalib.init_sqlite3(commonlib.pathlib.cur_file_dir('zqb_user.sqlite3'))

#for i in range(1,110):
#     zqb.capture_user_info(i)

#commonlib.capturedatalib.close_sqlite3()

#commonlib.capturedatalib.init_sqlite3(commonlib.pathlib.cur_file_dir('zqb_loan.sqlite3'))

#for i in range(1,254):
#     zqb.capture_loan(i)

#commonlib.capturedatalib.close_sqlite3()

commonlib.capturedatalib.init_sqlite3(commonlib.pathlib.cur_file_dir('zqb_loan_total.sqlite3'))

for i in range(1,40):
    zqb.capture_loan_total(i)

commonlib.capturedatalib.close_sqlite3()