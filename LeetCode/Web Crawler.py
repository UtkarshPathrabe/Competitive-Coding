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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        urls = set()
        def dfs(url):
            if url not in urls:
                urls.add(url)
                hostName = re.split('://|/', url)[1]
                newUrls = htmlParser.getUrls(url)
                for newUrl in newUrls:
                    if re.split('://|/', newUrl)[1] == hostName:
                        dfs(newUrl)
        dfs(startUrl)
        return list(urls)