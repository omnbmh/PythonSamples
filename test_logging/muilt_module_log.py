#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging

import moduleone

logger = logging.getLogger("main_module")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("log/muilt_module_log.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("create a instance of moduleone")


one = moduleone.ModuleOne()
logger.info("call class func")
one.dosome();

logger.info("call module func")
moduleone.dosomefunc()

logger.info("Done")