from typing import List


# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
class FontInfo(object):
   # Return the width of char ch when fontSize is used.
   def getWidth(self, fontSize, ch):
       """
       :type fontSize: int
       :type ch: char
       :rtype int
       """
       pass

   def getHeight(self, fontSize):
       """
       :type fontSize: int
       :rtype int
       """
       pass


class Solution:
    # Binary Search
    # check mid+1 and l=mid+1
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        hashmap = {}
        for c in text:
            hashmap[c] = hashmap.get(c, 0) + 1
        l, r = 0, len(fonts)-1
        while l < r:
            mid = (l+r) // 2
            w1, h1 = self.getWidthHeight(hashmap, fonts[mid+1], fontInfo)
            if w1 <= w and h1 <= h:
                l = mid+1
            else:
                r = mid
        w1, h1 = self.getWidthHeight(hashmap, fonts[l], fontInfo)
        return fonts[l] if w1 <= w else -1

    def getWidthHeight(self, hashmap, font, fontInfo):
        w = 0
        for c, count in hashmap.items():
            w += fontInfo.getWidth(font, c) * count
        h = fontInfo.getHeight(font)
        return w, h



if __name__ == '__main__':
    Solution().test()
