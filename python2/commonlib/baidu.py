#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import os
import sys
print os.name

'''
    百度
    百度贴吧自动签到
'''
import urllib
import http
import re
#import md5
import hashlib
import base64
import rsa
import json
import time

#百度 配置
BDUSS_FILE = 'load.bduss'
BAIDUID_FILE = 'load.baiduid'
SIGN_INTERVAL = 5

# baidu login http request paramters
client_id='_client_id=wappc_1368589871859_564'
client_type='_client_type=2'
client_version='_client_version=2.0.3'
phone_imei='_phone_imei='
net_type='net_type=3'
vcode_md5='vcode_md5='
pn='pn=1'

# baidu constants

#TT='tt=1454396078948'

class BaiduTieba(object):

    def __init__(self):
        self.token = self._get_token()
        self.bduss = self.__readbduss__()
        self.baiduid = self.__readbaiduid__()
        print (self.bduss,self.baiduid)

    def __paramparse__(self,param):
        # 将url上的参数 转换为dic
        print param
        str_arr = param.split('&')
        print str_arr
        body_data = {};
        for str in str_arr:
            temp_arr = str.split('=')
            body_data[temp_arr[0]]=temp_arr[1].encode('utf-8')
        print body_data
        return body_data

    def __readbduss__(self):
        #读取bduss信息
        if os.path.exists(os.path.join(cur_dir(),BDUSS_FILE)):
            print os.path.join(cur_dir(),BDUSS_FILE)

            with open(os.path.join(cur_dir(),BDUSS_FILE),'r') as f:
                # print type(f) # 注意系统变量 file
                bduss = f.read()
                bduss = bduss.strip("\r\n")
                return bduss
        return None

    def __readbaiduid__(self):
        #读取baiduid信息
        if os.path.exists(os.path.join(cur_dir(),BAIDUID_FILE)):
            print os.path.join(cur_dir(),BAIDUID_FILE)

            with open(os.path.join(cur_dir(),BAIDUID_FILE),'r') as f:
                # print type(f) # 注意系统变量 file
                baiduid = f.read()
                baiduid = baiduid.strip("\r\n")
                return baiduid
        return None

    def __writebduss__(self,bduss,baiduid):
        # 写入bduss信息
        file_object = open(os.path.join(cur_dir(),BAIDUID_FILE), 'w')
        file_object.write(baiduid)
        file_object.close()
        # 写入bduss信息
        file_object = open(os.path.join(cur_dir(),BDUSS_FILE), 'w')
        file_object.write(bduss)
        file_object.close()

    def _get_token(self):
        http.request('https://www.baidu.com/')
        # Token
        ret = http.request(
            'https://passport.baidu.com/v2/api/?getapi&tpl=pp' + \
            '&apiver=v3&class=login' + \
            '&gid=965D5E0-3500-4CE2-B4DC-8AA0D833BF6D&tt=%s&logintype=basicLogin&callback=0' % int(time.time())).replace('\'', '\"')
        foo = json.loads(ret)
        return foo['data']['token']

    def _get_publickey(self):
        url = 'https://passport.baidu.com/v2/getpublickey?token=' + \
            self.token
        content = http.request(url)
        jdata = json.loads(content.replace('\'','"'))
        return (jdata['pubkey'], jdata['key'])

    def _check_login_error(self,login_result):
        err_id = re.findall('err_no=([\d]+)', login_result)[0]
        code_string = re.findall('codeString=(.*?)&', login_result)[0]

        if err_id == '0':
            return (err_id,code_string)
        error_message = {
            '-1': u'系统错误, 请稍后重试',
            '1': u'您输入的帐号格式不正确',
            '3': u'验证码不存在或已过期,请重新输入',
            '4': u'您输入的帐号或密码有误',
            '5': u'请在弹出的窗口操作,或重新登录',
            '6': u'验证码输入错误',
            '16': u'您的帐号因安全问题已被限制登录',
            '257': u'需要验证码',
            '100005': u'系统错误, 请稍后重试',
            '120016': u'未知错误 120016',
            '120019': u'近期登录次数过多, 请先通过 passport.baidu.com 解除锁定',
            '120021': u'登录失败,请在弹出的窗口操作,或重新登录',
            '500010': u'登录过于频繁,请24小时后再试',
            '400031': u'账号异常，请在当前网络环境下在百度网页端正常登录一次',
            '401007': u'您的手机号关联了其他帐号，请选择登录'}
        try:
            msg = error_message[err_id]
        except:
            msg = 'unknown err_id=' + err_id
        print u'登录结果 - ' + msg
        return (err_id,code_string)

    def toString(self):
        pass

    def login_check(self,uname):
        url = 'http://wappass.baidu.com/wp/api/login/check?'
        # check used
        CLIENTFROM='clientfrom=native'
        GID='gid=BE56965-3AC1-4C07-9A86-F5E366F23BF8'

        data = CLIENTFROM + '&' + GID + '&tt=' + str(int(time.time()*1000)) + '&username='+uname
        data = http.request(url+data)
        print data


    def login(self,acc,pwd,vcode='',vcodestr=''):

        url = 'https://passport.baidu.com/v2/api/?login'
        pubkey , rsakey = self._get_publickey()

        #print pubkey
        #print rsakey
        key = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey)
        password_rsaed = base64.b64encode(rsa.encrypt(pwd, key))

        data = {}
        data[u'staticpage'] = 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html'
        data[u'charset'] = 'UTF-8'
        data[u'token'] = self.token
        data[u'tpl']='tb'
        data[u'subpro'] = ''
        data[u'apiver'] = 'v3'
        data[u'tt']=str(int(time.time()))
        data[u'codestring']=vcodestr
        data[u'safeflg'] = 0
        data[u'u']='https://passport.baidu.com/'
        data[u'isPhone'] = ''
        data[u'detect']= 1
        data[u'gid']='6A3375C-5CE5-4696-A8C2-8BBE62516FAF'
        data[u'quick_user']=0
        data[u'logintype']='basicLogin'
        data[u'logLoginType']= 'pc_loginBasic'
        data[u'idc']=''
        data[u'loginmerge']='true'
        data[u'username']=acc
        data[u'password']=password_rsaed
        data[u'verifycode'] = vcode
        data[u'rsakey']=rsakey
        data[u'crypttype']=12
        data[u'countrycode']=''
        data[u'callback']=0

        # start login
        data=http.request(url,data)
        #data=json.loads(data)
        err_no,code_string = self._check_login_error(data)
        '''
        if data[u'errInfo'][u'no']=='0':
            #login success & need save bduss
            bduss=data['user']['BDUSS'].encode('utf-8')
            bduss = 'BDUSS='+bduss.decode()
            self.__writebduss__(bduss)
        '''
        '''
        if data[u'errInfo'][u'no']=='500001':
            url = 'http://wappass.baidu.com/cgi-bin/genimage?'+data[u'data'][u'codeString'] + '&v='+str(int(time.time()*1000))
            http.download(url,cur_dir()+u'/',u'vcode.jpg')
            vc = raw_input('请输入验证码:')
            return self.login(baiduUtf(acc),base64.b64encode(pwd.encode('utf-8')).decode(),vc,data[u'data'][u'codeString'])
        '''
        # 是否需要验证码
        if err_no=='257' or err_no=='6' :
            url = 'https://passport.baidu.com/cgi-bin/genimage?'+ code_string + '&v='+str(int(time.time()*1000))
            http.download(url,cur_dir()+u'/',u'vcode.jpg')
            vc = raw_input('请输入验证码:')
            self.login(acc,pwd,vc,code_string)
        if err_no=='0':
            # bduss = None
            for item in http.cookies():
                if item.name == 'BDUSS':
                    self.bduss = item.value
                if item.name == 'BAIDUID':
                    self.baiduid = item.value
            #self.bdauth = 'BAIDUID=' + self.baiduid + '; BDUSS=' + self.bduss
            #print self.bdauth
            self.__writebduss__(self.bduss,self.baiduid)
            print 'relogin access!'

    def is_login(self):
        if (not self.bduss) or (not self.baiduid):
            print 'login fail!'
            return False
        self.bdauth = 'BAIDUID=' + self.baiduid + '; BDUSS=' + self.bduss
        url='http://tieba.baidu.com/dc/common/tbs'
        data=http.request(url,cookie=self.bdauth)
        k=json.loads(data)
        if k["is_login"]==1:
            print 'login success!'
            return True
        else:
            print 'login fail!'
            return False

    def tieba_list(self):
        # 获取关注的贴吧列表
        url="http://c.tieba.baidu.com/c/f/forum/favolike"
        singbase= 'BDUSS='+self.bduss +'&'+ client_id+'&'+ client_type+'&'+ client_version+'&'+ phone_imei+'&'+ net_type+'&'+ pn
        signmd5= 'BDUSS='+self.bduss + client_id+ client_type+ client_version+ phone_imei+ net_type+ pn
        sign = '&sign=' + hashlib.md5((signmd5+'tiebaclient!!!').encode()).hexdigest()
        data=singbase+sign
        data=http.request(url,self.__paramparse__(data))
        tieba = []
        data=json.loads(data)
        list=data['forum_list']
        for x in list:
            tieba.append(x['name'].encode('gbk'))
        tbs='tbs='+data['anti']['tbs']
        return [tieba,tbs]

    def sign(self):
        tieba = self.tieba_list()
        url='http://c.tieba.baidu.com/c/c/forum/sign'
        tbs = tieba[1]
        for x in  tieba[0]:
            kw='kw='+x.decode('gbk')
            sign='&sign='
            signmd5= 'BDUSS='+self.bduss + kw + tbs + 'tiebaclient!!!'
            signbase= 'BDUSS='+self.bduss +'&'+ kw + '&' + tbs
            sign=sign+hashlib.md5(signmd5.encode('utf-8')).hexdigest()
            data=signbase+sign
            data=http.request(url,self.__paramparse__(data))
            data=json.loads(data)
            if data['error_code']=='0':
                print x , u'吧 签到成功！'
            else:
                print x , u'吧 签到失败！ 失败原因:' , data['error_msg'].encode('gbk')
            time.sleep(float(SIGN_INTERVAL))

def baiduUtf(data):
    datagb=data.decode("gbk")
    return urllib.quote_plus(datagb.encode('UTF-8'))
    #return urllib.parse.quote(datagb.encode('utf-8'))
    #return datagb
def cur_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

if __name__ == '__main__':
    tieba = BaiduTieba()
        #if tieba.is_login():
    #tieba.sign()
    #tieba.login_check('1649123641264917392491646294')
    tieba.login('deathwingo','ymd')
