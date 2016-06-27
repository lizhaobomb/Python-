import urllib
import sgmllib


class HandleHtml(sgmllib.SGMLParser):
    def unknown_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "href":
                print attr[0]+":"+attr[1].encode('utf-8')

    def unknown_endtag(self, tag):
        print "----------" + tag + "-----------"


web = urllib.urlopen("http://freebuf.com/")
web_handler = HandleHtml()

web_handler.feed(web.read())
