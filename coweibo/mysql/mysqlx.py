#! /usr/bin/python
#-*- coding:utf-8 -*-

import os
import os.path
import ConfigParser
import mysql.connector

base_dir = os.path.dirname(__file__)
print "base_dir " + base_dir
config = ConfigParser.ConfigParser()
config.readfp(open(base_dir + "/mysql.ini"),"rb")
mode = config.get("global","mode")

MYSQL_CONFIG = {}
MYSQL_CONFIG["host"] = config.get("mysql/" + mode, "host")
MYSQL_CONFIG["port"] = config.get("mysql/" + mode, "port")
MYSQL_CONFIG["user"] = config.get("mysql/" + mode, "user")
MYSQL_CONFIG["password"] = config.get("mysql/" + mode, "password")
MYSQL_CONFIG["database"] = config.get("mysql/" + mode, "database")
MYSQL_CONFIG["charset"] = config.get("mysql/" + mode, "charset")

print MYSQL_CONFIG

def search(sql):
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        count = cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        return results
    except mysql.connector.Error as e:
        print 'connect fails!{}'.format(e)
    else:
        pass
    finally:
        conn.close()
    
def update(sql):
    pass