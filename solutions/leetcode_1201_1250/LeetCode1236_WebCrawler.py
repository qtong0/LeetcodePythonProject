# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """
       pass


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser'):
        queue = [startUrl]
        hostName = self.getHostName(startUrl)
        res = []
        visited = set([startUrl])
        while queue:
            url = queue.pop(0)
            res.append(url)
            for nextUrl in htmlParser.getUrls(url):
                if nextUrl not in visited and hostName == self.getHostName(nextUrl):
                    visited.add(nextUrl)
                    queue.append(nextUrl)
        return res

    def getHostName(self, url):
        s = url.lstrip("http://")
        arr = s.split("/")
        return arr[0]
