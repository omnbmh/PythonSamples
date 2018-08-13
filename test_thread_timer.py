# -*- coding:utf-8 -*-

"""
使用threading Timer 实现定时功能

"""
import threading
import time


def hello(name):
    print("hello " + name + "!")
    time.sleep(1)
    timer = threading.Timer(2.0, hello, ["W~Sir"])
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(2.0, hello, ["W~Sir"])
    timer.start()
