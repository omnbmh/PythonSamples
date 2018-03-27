#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging

mo_logger = logging.getLogger("main_module.one")


class ModuleOne():
    def __init__(self):
        self.logger = logging.getLogger("main_module.one.module")
        self.logger.info("creating an instance in ModuleOne")

    def dosome(self):
        self.logger.info("func dosame execute in class")


def dosomefunc():
    mo_logger.info("func dosamefunc execute")
