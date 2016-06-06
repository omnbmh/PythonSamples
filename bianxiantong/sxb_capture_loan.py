#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- author: c8d8z8@gmail.com

import commonlib.http
import commonlib.capturedatalib
import commonlib.pathlib
import json
import time

page = 0
page_size = 30

def capture(page,page_size):
    url = 'https://www.itoumi.com/sxb/products/loans.json'
    data = {}
    data['url'] = 'products/loans.json'
    data['prodNo'] = '20150811163740805506'
    data['startId'] = page * page_size + 1
    data['maxRecords'] = page_size

    rt = commonlib.http.request(url,data)
    jrt = json.loads(rt)
    time.sleep(float(1))
    loans = jrt['debtList']
    #print jrt
    for loan in loans:
        #print loan
        #print json.dumps(data)
        print json.dumps(loan,ensure_ascii=False)
        store_data = {}
        store_data['req_param'] = json.dumps(data)
        store_data['json_data'] = json.dumps(loan,ensure_ascii=False)
        store_data['req_url'] = url
        
        commonlib.capturedatalib.save2sqlite3(store_data)

commonlib.capturedatalib.init_sqlite3(commonlib.pathlib.cur_file_dir('sxb_loan.sqlite3'))
for i in range(1757,2457):
    capture(i,page_size)

commonlib.capturedatalib.close_sqlite3()
