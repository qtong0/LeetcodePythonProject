from typing import List


class Solution(object):
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for w in words:
            if self.isStretchy(S, w):
                res += 1
        return res
    
    def isStretchy(self, s0, s1):
        m, n = len(s0), len(s1)
        i, j = 0, 0
        while i < m and j < n:
            if s0[i] != s1[j]:
                return False
            s0BlockSize = 1
            i += 1
            while i < m and s0[i-1] == s0[i]:
                s0BlockSize += 1
                i += 1
            s1BlockSize = 1
            j += 1
            while j < n and s1[j-1] == s1[j]:
                s1BlockSize += 1
                j += 1
            if s0BlockSize < s1BlockSize or (s1BlockSize < s0BlockSize < 3):
                return False
        return i == len(s0) and j == len(s1)
    
    def test(self):
        testCases = [
            [
                "heeellooo",
                ["hello", "hi", "helo"]
            ],
            [
                "zzzzzyyyyy",
                ["zzyy","zy","zyy"],
            ],
            [
                "dddiiiinnssssssoooo",
                ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"],
            ],
        ]
        for s, words in testCases:
            print('s: %s' % s)
            print('words: %s' % words)
            result = self.expressiveWords(s, words)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
