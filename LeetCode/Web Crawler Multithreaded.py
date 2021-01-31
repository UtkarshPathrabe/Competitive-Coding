# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
def getHostName(url: str) -> str:
    return url.split('/')[2:3]

from threading import Thread

class URLFetch(Thread):
    def __init__(self, url: str, hostName: str, htmlParser: 'HtmlParser'):
        Thread.__init__(self)
        self.url = url
        self.hostName = hostName
        self.htmlParser = htmlParser
        self.urls = set()
        
    def run(self):
        self.urls = set([u for u in self.htmlParser.getUrls(self.url) if getHostName(u) == self.hostName])

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostName = getHostName(startUrl)
        queue, visited = [startUrl], set([startUrl])
        while queue:
            nextUrls = set()
            threads = [URLFetch(url, hostName, htmlParser) for url in queue]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
                nextUrls |= thread.urls
            nextUrls -= visited
            visited |= nextUrls
            queue = nextUrls
        return visited