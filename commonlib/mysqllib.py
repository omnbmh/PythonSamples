#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import ConfigParser
import mysql.connector

def configure(config):
    try:
        #print(config)
        conn = mysql.connector.connect(**config)
        print 'connect successfully!'
    except mysql.connector.Error as e:
        print 'connect fails!{}'.format(e)

def file_configure(fpath):
    config = ConfigParser.ConfigParser()
    config.readfp(open(fpath),"rb")
    mode = config.get("global","mode")
    MYSQL_CONFIG = {}
    MYSQL_CONFIG["host"] = config.get("mysql/" + mode, "host")
    MYSQL_CONFIG["port"] = config.get("mysql/" + mode, "port")
    MYSQL_CONFIG["user"] = config.get("mysql/" + mode, "user")
    MYSQL_CONFIG["password"] = config.get("mysql/" + mode, "password")
    MYSQL_CONFIG["database"] = config.get("mysql/" + mode, "database")
    MYSQL_CONFIG["charset"] = config.get("mysql/" + mode, "charset")
    configure(MYSQL_CONFIG)

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

def insert_req_to_musql(data,url,param):
    sql_data = {}

    print json.dumps(data,ensure_ascii=False,indent=2)

    sql_data['json_data'] = json.dumps(data,ensure_ascii=False,indent=2)
    sql_data['snap_date'] = datetime.datetime.now()
    sql_data['req_url'] = url
    sql_data['req_param'] = param

    sql = '''
        insert into `json_data`(`json_data`,`snap_date`,`req_url`,`req_param`) values (%(json_data)s,%(snap_date)s,%(req_url)s,%(req_param)s)
        '''
    mysqllib.execute(sql,sql_data)
    mysqllib.commit()
    print 'request insert into mysql complete.'

if __name__ == '__main__':
    #config = {'host':'127.0.0.1',
    #'user':'test',
    #'password':'123456',
    #'port':3306,
    #'database':'test',
    #'charset':'utf8'}
    #configure(config)

    file_configure('mysql.ini')
