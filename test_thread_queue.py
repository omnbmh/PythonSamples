# -*- coding:utf-8 -*-

"""
使用Queue管理线程

"""
import threading
import time


def do_job(ram_num):
    print("tt_" + str(ram_num) + " running!")
    time.sleep(1)


if __name__ == "__main__":
    threads = []
    for i in range(100, 1000, 200):
        tt = threading.Thread(target=do_job, name='tt_' + str(i), args=(i,))
        threads.append(tt)

    for t in threads:
        t.start()

    for t in threads:
        # t.join()
        if t.isAlive():
            print(t.name + " join")
            t.join()
