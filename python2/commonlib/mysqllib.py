#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import mysql.connector

config = {'host':'10.106.89.104','user':'root','password':'123456','port':8806,'database':'test','charset':'utf8'}

try:
    #conn = mysql.connector.connect(**config)
    print 'connect successfully!'
except mysql.connector.Error as e:
    print 'connect fails!{}'.format(e)


def execute(sql,data):
    cursor = conn.cursor()
    try:
        result = cursor.execute(sql,data)
        
        return result
    except mysql.connector.Error as e:
        print 'mysql execute error !{}'.format(e)
    finally:
        cursor.close()
def create():
    pass
def update():
    pass
def read():
    pass
def delete():
    pass

def commit():
    conn.commit()
