#codeing=utf-8
import os

print( "cwd " + "-"*10 + " " + os.getcwd())

def writeToken():
	f = open("token","a+")
	f.write("1902435213 2.00vS7kECWuBs3D96312aaa20hsGmUE")
	f.write("\n")
	#f.write("3194208571 2.00FZZKUDWuBs3D943817e4cd5SHx3E")
	#f.write("\n")
	f.close()

import mysql.connector, urllib.request, json, time

config={'host':'192.168.8.240',
	'user':'root',
	'password':'123456',
	'port':3307,
	'database':'test',
	'charset':'utf8'
	}

try:
	conn = mysql.connector.connect(**config)
	
except mysql.connector.Error as e:
	conn.close()
	print('connect fails!{}'.format(e))
else:
	pass
finally:
	pass

def buildInsertOrUpdateSql():
	return "INSERT INTO {table} VALUES ({id}, '{text}', '{source}', '{geo}', {reposts_count}, {comments_count}, '', '{created_at}', {uid}, {ori_id}, {ori_uid}) ON DUPLICATE KEY UPDATE id = {id}"

def run():
	print('let\'s go')
	# read user 
	f = open('token','r')
	for l in f.readlines():
		u = l.strip()
		print('current user ' + u)
		uid = u.split(' ',)[0]
		token = u.split(' ',)[1]
		# check user table 
		cursor = conn.cursor()
		cursor.execute("show tables like 'u_"+uid+"'")
		is_ = cursor.fetchall()
		if not len(is_) :
			# create table
			cursor.execute("SHOW CREATE TABLE test.u_0")
			createTableSql = cursor.fetchone()
			sql = createTableSql[1].replace('_0','_'+uid)
			cursor.execute(sql)
			#cursor.commit()
		cursor.close()
		
		s = urllib.request.urlopen('https://api.weibo.com/2/statuses/user_timeline.json?access_token='+token+'&uid='+uid).read().decode()
		# convert to json 
		weibos = json.loads(s)
		
		# update database
		cursor = conn.cursor()
		if 'error_code' in weibos :
			print(weibos['error_code'])
		else:
			print("current req statuses " + str(len(weibos['statuses'])))
			if weibos['statuses'] :
				# build sql 
				for weibo in weibos['statuses']:
					# add args table ori_id ori_uid
					weibo['table'] = 'u_' + uid
					weibo['ori_id'] = '0'
					weibo['ori_uid'] = '0'
					weibo['uid'] = weibo['user']['id']
					
					# Tue May 31 17:46:55 +0800 2011
					t = time.strptime(weibo['created_at'],'%a %b %d %H:%M:%S %z %Y')
					weibo['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S',t)
					sql_e = buildInsertOrUpdateSql().format(**weibo)
					#print(sql_e)
					cursor.execute(sql_e)
				conn.commit()
				cursor.close()
	print('oKay')
run()
