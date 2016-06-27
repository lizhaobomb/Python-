
# -*- encoding:utf-8 -*-
import urllib2
import re

class GitHubTrend:
    # http://www.jianshu.com/search?q=iOS&type=collections&page=2
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {"User-Agent":self.user_agent}

    def getPage(self):
        try:
            pageUrl = "https://github.com/trending?l=objective-c&since=monthly"
            request = urllib2.Request(pageUrl,headers=self.headers)
            response = urllib2.urlopen(request)
            pageContent = response.read().decode('utf-8')
            # print pageContent
            return pageContent
        except urllib2.URLError, e:
            print u"连接github失败,失败原因:", e.reason
            return None

    def getCollection(self):
        prefix = "https://github.com/"
        pageContent = self.getPage()
        pattern = '<span class="prefix">(.*?)</span>.*?</span>(.*?)</a>.*?<p class="repo-list-description">(.*?)</p>'
        allTitles = re.findall(pattern,pageContent,re.S)
        # print allTitles
        for title in allTitles:
            print u"%s/%s \n描述:%s \n链接:%s%s/%s%s" %(title[0],title[1].strip().replace('\n', ''),
                                                        title[2].strip().replace('\n', ''),
                                                        prefix,title[0],title[1].strip().replace('\n', ''),".git")
        return allTitles
trend = GitHubTrend()
trend.getCollection()



