#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import commonlib.http
import commonlib.path
import commonlib.systeminfo
import json

login_url = 'http://www.fact-eye.com:9000/dl/dl_easy_login.htm?ajaxSession=E2C47E6B2A047C6DE780C28911293B7F'
data_url = 'http://www.fact-eye.com:9000/dl/agent_Statistics_ajax.htm'

def login():
    data = 'userID=wzj&userPW=1234567890&agentId=01&agentName=%E4%B8%8A%E5%B7%A5%E5%8C%BB%E4%BF%A1&agentUrl=sgyx'
    data = commonlib.http.request(login_url,commonlib.http.paramparse(data))
    data=json.loads(data)
    print data
    if len(data) > 0:
        print data[0][u'resultMsg'].encode(commonlib.systeminfo.os_coding)
        if data[0][u'result'] == u'true':
            print u'登陆成功!'.encode(commonlib.systeminfo.os_coding)
            return True
    return False
    
def capture_data(dd,page):
    data_fmt = 'submitFlg=3&page=%s&flg=M&allFlg=&agentId=01&agenterId=&date=%s 00:00:00&selectDayFlg=1'
        
    if page == None:
        page = 1
    print (u'开始查询日期为' + data_date + u'第' + str(page) + u'页').encode(commonlib.systeminfo.os_coding)
    data = data_fmt % (str(page),data_date)
    data = commonlib.http.request(data_url,commonlib.http.paramparse(data))
    data=json.loads(data)
    #print data
    if len(data) > 0:
        if data[0][u'result'] == u'true':
            print u'抓取成功!'.encode(commonlib.systeminfo.os_coding)
            list_data = data[0][u'list']
            print list_data.encode(commonlib.systeminfo.os_coding)
            data_arr = list_data.split('@')
            # len 7, 0 hospital 1 number 2 t_page 3 cur_page
            #print data_arr
            save_data(data_arr[0],data_arr[1],dd)
            if(data_arr[3] != data_arr[2]):
                capture_data(dd,page+1)
            
def save_data(names,numbers,dd):

    name_arr = names.split(',')
    number_arr = numbers.split(',')
    file = open(commonlib.path.cur_file_dir(u'yanzhuzi-statistics-data.txt'),'a')
    for idx in range(0,9+1):
        if len(name_arr[idx]) > 0:
            file_data = '%s    %s    %s' % (name_arr[idx],number_arr[idx],dd)
            print file_data
            file.write(file_data.encode(commonlib.systeminfo.os_coding)+'\n')
    file.close()
        
if __name__ == '__main__':
    if login():
        for i in range(2014,2016+1):
            for j in range(1,12+1):
                data_date = str(i) + str(j).zfill(2)
                capture_data(data_date,None)