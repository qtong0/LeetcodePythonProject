from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ''
        for s0 in dictionary:
            if self.isValid(s, s0):
                if len(s0) > len(res) or (len(s0) == len(res) and s0 < res):
                    res = s0
        return res

    def isValid(self, s1, s2):
        j = 0
        for c in s1:
            if c == s2[j]:
                j += 1
                if j == len(s2):
                    return True
        return False
