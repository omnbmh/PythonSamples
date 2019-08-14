#!/bin/python
# -*- coding:utf-8 -*-

'''
抓取花椒推荐页面小姐姐信息
'''

import requests
from bs4 import BeautifulSoup
import re
import time
import json

DEBUG = True

''' 常用 url 备注

'''


def printUrl():
    pass


def get_page():
    live_ids = set()
    url = "http://www.huajiao.com/category/800"
    url = "http://www.huajiao.com/category/1000"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', href=re.compile('^(/l/)')):
        href = link.attrs['href'][3:]  # link是标签，取它的属性
        live_ids.add(href)
    # /l/1234567890
    return live_ids


def get_user_id(live_id):
    try:
        headers = {"User-Agent": "curl/7.54.0"}
        print('live page url - ' + 'http://www.huajiao.com/l/{}'.format(live_id))
        response = requests.get('http://www.huajiao.com/l/{}'.format(live_id), headers=headers)
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取 页面的 title 属性 包含用户Id
        text = soup.title.get_text()

        # print(text)
        userId = re.findall('(\w+:\d+)', text)

        if len(userId) == 0:
            print("--- live closed ")
            return None
        else:
            # ID:1234567890
            return userId[0][3:]
    except Exception as e:
        print(e)


def get_user_info(user_id):
    url = 'http://www.huajiao.com/user/{}'.format(user_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    ss = soup.find_all("script")

    for scpt in ss:
        # print(scpt.text)
        '''
        window._USERCONTENT = {
        userList: [],
        action: 'user_home',
        fansrankApi: "//webh.huajiao.com/fansrank",
        uid: "199435322", 
        userInfo: {"uid":"199435322","nickname":"\u871c\u871c\u5927\u738b\ud83c\udf51","avatar":"http:\/\/image.huajiao.com\/a281dd8e33398108df9c95b0d1c3456c-100_100.jpg","avatar_m":"http:\/\/image.huajiao.com\/a281dd8e33398108df9c95b0d1c3456c-324_324.jpg","avatar_l":"http:\/\/image.huajiao.com\/a281dd8e33398108df9c95b0d1c3456c-640_640.jpg","avatar_o":"http:\/\/image.huajiao.com\/a281dd8e33398108df9c95b0d1c3456c.jpg","signature":"\u813e\u6c14\u53e4\u602a\ud83d\ude0f","gender":"F","astro":"\u5929\u874e\u5ea7","location":"\u6c5f\u82cf \u65e0\u9521","lives":0,"watches":0,"praises":"1366240","followings":"0","followers":"14994","verified":false,"verifiedinfo":{"credentials":"\u813e\u6c14\u53e4\u602a\ud83d\ude0f","type":0,"realname":"\u871c\u871c\u5927\u738b\ud83c\udf51","status":0,"error":"","official":false},"vrid":"","isbindvr":false,"source":"mobile","forbidden":false,"exp":43410,"authorexp":9118,"charmexp":315143,"level":12,"authorlevel":9,"charmlevel":32,"medal":[],"cached":true,"cachetime":1565760790,"addtime":1561278963,"apc":false,"iscert":true,"isadult":true,"iden_source":"\u5e73\u53f0","iden_source_ext":"","mbregion":"\u4e2d\u56fd","mbcode":"+86","lasttime":0,"online":0,"birthday":"1995-11-09","display_uid":"","is_modify_gender":false,"shortlive":false,"charm_linked":true,"followed":false,"blocked":false,"effect":"","is_author_task":1,"is_welfare":0,"since_reg":52,"hidden_privilege":{"message":"\u81f3\u5c0a\u738b\u8005\u5f00\u542f","url":"https:\/\/h.huajiao.com\/static\/html\/noble\/index.html"},"isfriend":false,"online_duration":"","distance":"","feeds":"3","tags":{"impressions":["\u6027\u611f","\u597d\u8eab\u6750","\u5973\u795e"],"occupation":["\u5168\u804c\u4e3b\u64ad"],"live":["\u97f3\u4e50"]},"signature_style":false,"border_style":"http:\/\/image.huajiao.com\/0036821d86d7a391d9b0a6bcb6dab5be.jpg","es_nickname":"\u871c\u871c\u5927\u738b\ud83c\udf51","pocket":null}
        };
        '''
        if re.match(".*" + user_id, scpt.text, flags=re.DOTALL):
            print(str(scpt.text.decode('utf-8')))
            print(type(scpt.text))

            print(json.dumps(re.findall(r'userInfo:\s\{.*?\};', scpt.text, flags=re.DOTALL)[0][10:-1]))

            print('---- get')
            print(re.findall(r'\"nickname\":\".*?\"', scpt.text))
            print(re.findall(r'\"signature\":\".*?\"', scpt.text))
            print(re.findall(r'\"gender\":\".*?\"', scpt.text))
            print(re.findall(r'\"location\":\".*?\"', scpt.text))
            print(re.findall(r'\"lives\":\d+', scpt.text))
            print(re.findall(r'\"followings\":\".*?\"', scpt.text))
            print(re.findall(r'\"followers\":\".*?\"', scpt.text))
            print(re.findall(r'\"verified\":.*?', scpt.text))
            print(re.findall(r'\"exp\":\d+', scpt.text))
            print(re.findall(r'\"addtime\":\d+', scpt.text))
            print(re.findall(r'\"lasttime\":\d+', scpt.text))
            print(re.findall(r'\"feeds\":\".*?\"', scpt.text))
            return

    print("--- ERROR get_user_info")


# feeds
def get_user_json_info(user_id):
    if not user_id:
        return None
    print('--- get_user_json_info user_id' + user_id)
    try:
        url = 'http://webh.huajiao.com/User/getUserFeeds'
        ts = str(int(time.time() * 1000))
        data = {
            # _callback: jQuery110205725579475666431_1557985426506
            'fmt': 'jsonp',
            'uid': user_id,
            'offset': None,
            '_': ts
        }
        headers = {
            'Referer': 'http://www.huajiao.com/v/182532937',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }

        response = requests.get(url, params=data, headers=headers)
        content = response.json()
        return content
    except Exception as e:
        print('---ERROR get_user_json_info user_id' + user_id)
        print(e)


def output_live_url(user_json_info):
    if not user_json_info:
        return

        # print(json.dumps(user_json_info))
    print('errno ' + str(user_json_info[u'errno']))

    if len(user_json_info[u'data']) > 0 and len(user_json_info[u'data'][u'feeds']) > 0:
        f = user_json_info[u'data'][u'feeds'][0]

        title = f[u'feed'][u'title']
        publishtime = f[u'feed'][u'publishtime']
        if u'sn' in f[u'feed']:
            sn = f[u'feed'][u'sn']
            channel = f[u'relay'][u'channel']
            print('title: ->' + title + '<- publishtime: ' + publishtime + ' relay channel: ' + channel + ' sn ' + sn)
            print('--- live video url ---')
            print(re_live_url_prefix(sn) + '/' + channel + '/' + sn + '.flv')
        else:
            print('--- no live video url ---')

    else:
        print('--- no feeds info ---')

    # for f in user_json_info[u'data'][u'feeds']:
    #     print('title ' + f[u'feed'][u'title'])
    #     print('publishtime ' + f[u'feed'][u'publishtime'])
    #     if u'sn' in f[u'feed']:
    #         print('sn ' + f[u'feed'][u'sn'])
    #         print('relay channel ' + f[u'relay'][u'channel'])
    #         # print('sn ' + f[u'feed'][u'sn'])
    #     else:
    #         print('watermark ' + f[u'feed'][u'watermark'])


def re_live_url_prefix(sn):
    url = "http://{}.live.huajiao.com"
    if re.match(".*AL1", sn):
        return url.format("al1-flv")
    if re.match(".*AL2", sn):
        return url.format("al2-flv")
    if re.match(".*QH1", sn):
        return url.format("qh1-flv")
    if re.match(".*QH2", sn):
        return url.format("qh2-flv")
    if re.match(".*ps3", sn):
        return url.format("pl3")
    if re.match(".*ps4", sn):
        return url.format("pl4")
    # if re.match(".*AL1", sn):
    #     return url.format("al1-flv")
    print('not match sn: ' + sn)
    return url


USER_ID_LIST = [199435322, 202056049, 34902450, 118408961, 113844274, 33108561, 123871591, 198921621, 199205677,
                128572418]
if __name__ == "__main__":
    # get_user_id('286790593')
    # for user_id in USER_ID_LIST:
    #     # output_live_url(get_user_json_info(str(user_id)))
    #     get_user_info(str(user_id))
    #     break

    output_live_url(get_user_json_info("198163856"))

    # for i in get_page():
    #     # printUrl('');
    #
    #     user_id = get_user_id(i)
    #     print("--- live_id " + i + "--- user_id " + user_id)
    #     user_json_info = get_user_json_info(user_id)
    #     output_live_url(user_json_info)
    #     print('--- end ---')
