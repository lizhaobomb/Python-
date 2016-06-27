#-*- coding: UTF-8 -*-
__author__ = 'lizhao'

import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK:
    #初始化方法,定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = {'User-Agent': self.user_agent}
        #存放段子的变量,每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页的索引获得页面的代码
    def getPage(self,pageIndex):
            try:
                url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
                #构建请求的request
                request = urllib2.Request(url,headers = self.headers)
                #利用urlopen获取页面代码
                response = urllib2.urlopen(request)
                #将页面转化为UTF-8编码
                pageCode = response.read().decode('utf-8')
                return pageCode
            except urllib2.URLError, e:
                if hasattr(e,"reason"):
                    print u"连接糗事百科失败,错误原因",e.reason
                    return None



    #传入某一页代码,返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print u"页面加载失败....."
            return None
        pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?title="(.*?)">.*?</a>.*?<div.*?class' +
                             '="content.*?>(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',
                             re.S)
        items = re.findall(pattern, pageCode)
        #用来存储每页的段子们
        pageStroies = []
        for item in items:
            haveImg = re.search("img", item[2])
            # dr = re.compile(r'<[^>]+>', re.S)
            # dd = dr.sub('', item[1])
            # print dd
            if not haveImg:
                #print item[0], item[1], item[3]
                #item[0]发布者,item[1]内容,item[3]点赞数
                pageStroies.append([item[0].strip(),item[1].replace('<br/>','\n').strip(),item[3].strip()])
                return pageStroies

     # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        if self.enable == True:
            if 2 > len(self.stories):
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                print u"程序退出谢谢观看"
                self.enable = False
                return
            print u"第%d页\t发布人:%s\n%s\n赞:%s\n" %(page,story[0],story[1],story[2])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
spider = QSBK()
spider.start()

