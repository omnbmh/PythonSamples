#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- author: c8d8z8@gmail.com


import sqlite3

#conn = None

def save2mysql(data):
    pass


def init_sqlite3(sqlite_db_name):
    global conn
    conn = sqlite3.connect(sqlite_db_name)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS json_data (json_data varchar(5000),req_url varchar(500),req_param varchar(500))')
    return conn

def save2sqlite3(data):
    #print sqlite_db_name
    t = (data['json_data'],data['req_url'],data['req_param'])
    #print t
    #t['json_data'] = data['json_data']
    #t['req_url'] = data['req_url']
    #t['req_param'] = data['req_param']
    global conn
    
    cur = conn.cursor()
    cur.execute('insert into json_data values (?,?,?)',t)
    conn.commit()
    print 'save2sqlite3 complete!'

def close_sqlite3():
    global conn
    conn.close()
