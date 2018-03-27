#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket
import sys
import time

import psutil

CMD = "C:\\eth-support\\ethminer-0.13.0-Windows\\bin\\ethminer --farm-recheck 200 -U --cuda-parallel-hash 4 -SP 1 -F  http://127.0.0.1:60006/eth01 --cuda-devices 0 1 2 3 4 5 --api-port 3333"


def main():
    if not check_process():
        start()
    else:
        print 'program is running!!!'

    while True:
        try:
            resp = miner_getstat1()
            print resp
            time.sleep(60)
        except Exception, e:
            print e.args
            restart()


def start():
    psutil.Popen(CMD)
    time.sleep(30)
    print "Program ethminer startup!!!"


def restart():
    name = 'ethminer.exe'
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == name:
            p.terminate()
            print 'ethminer killed!!!'
            timesleep(10)
            start()
            break
    print 'ethminer restart ok!!!'


def check_process():
    name = 'ethminer.exe'
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == name:
            return p


def miner_getstat1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)  # 10 s
    s.connect(('localhost', 3333))
    s.sendall('{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}\n'.encode('utf-8'))
    resp = ''
    while 1:
        data = s.recv(4096)
        resp += data.decode('utf-8')
        if not data or (len(data) < 4096 and data[-3:] == b']}\n'):
            break
    s.close()
    return resp


def print_data(data_str):
    pass


if __name__ == "__main__":
    # print miner_restart()
    # print miner_getstat1()
    main()
