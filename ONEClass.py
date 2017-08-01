__author__ = "zichen0422"

# * tips *
# -*- coding: utf-8 -*-

import urllib2
import urllib
import json
import uuid

class ONE_class:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def splitAuthor(self, author):
        if author:
            print author['user_name']
            print author['desc']
            print author['wb_name']
            print author['summary']
            print author['web_url']
    
    def splitShareInfo(self, shareInfo):
        print 'share info'
    
    def splitSharelistInfo(self, info):
        print info['title']
        print info['desc']
        print info['link']
        print info['imgUrl']
        print info['audio']

    def splitShrelist(self, sharelist):
        self.splitSharelistInfo(sharelist['wx'])
        #self.splitSharelistInfo(sharelist['wx_timeline'])
        #self.splitSharelistInfo(sharelist['weibo'])
        #self.splitSharelistInfo(sharelist['qq'])

    def splitContentData(self, content):
    
        for k in range(0,len(content)):
            print '--------------------------'
            print content[k]['title']
            print content[k]['forward']
            self.splitAuthor(content[k]['author'])
            self.splitShrelist(content[k]['share_list'])
    
    def start(self):
        request = urllib2.Request(self.baseUrl)
        response = urllib2.urlopen(request)
        re = json.loads(response.read().decode('utf-8')) 
        print re['res']
        print re['data']['id']
        print re['data']['date']
        #weather
        #print re['data']['weather']
        print re['data']['weather']['city_name']
        print re['data']['weather']['date']
        print re['data']['weather']['temperature']
        print re['data']['weather']['humidity']
        print re['data']['weather']['climate']
        print re['data']['weather']['wind_direction']
        print re['data']['weather']['hurricane']

        print '----- start split content Data -----' 
        self.splitContentData(re['data']['content_list'])
        

print '----- start python ------'
#print uuid.uuid1()
uid = str(uuid.uuid1())
userId = raw_input("please input useid     ")

baseUrl = "http://v3.wufazhuce.com:8000/api/onelist/4360/%E6%B7%B1%E5%9C%B3%E5%B8%82?platform=ios&uuid=" + uid + "&user_id=" + userId + "&version=v4.2.2"
print baseUrl

#baseUrl = "http://v3.wufazhuce.com:8000/api/onelist/4360/%E6%B7%B1%E5%9C%B3%E5%B8%82?platform=ios&uuid=xxxxxxxxxxxxxxxxx&user_id=xxxxxxx&version=v4.2.2"
oneClass = ONE_class(baseUrl)
oneClass.start()

# next page -> more/XXXX?  XXXX ->array id
#GET http://v3.wufazhuce.com:8000/api/channel/reading/more/0?platform=ios&uuid=xxxxxxxxxxxxxxx&user_id=xxxxxxx&version=v4.2.2