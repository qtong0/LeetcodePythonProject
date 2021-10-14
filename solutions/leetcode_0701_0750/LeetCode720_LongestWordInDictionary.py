from typing import List


class Solution(object):
    def longestWord(self, words: List[str]) -> str:
        res = ''
        words.sort()
        # visited
        hashset = set()
        for w in words:
            if len(w) == 1 or w[:len(w)-1] in hashset:
                if len(w) > len(res):
                    res = w
                hashset.add(w)
        return res


    def longestWord_another(self, words: List[str]) -> str:
        if not words: return ''
        words.sort(key=len)
        n = len(words[-1])
        dp = [set() for _ in range(n+1)]
        for word in words:
            if len(word) == 1 or word[:-1] in dp[len(word)-1]:
                dp[len(word)].add(word)
        for i in range(n, -1, -1):
            if dp[i]:
                return sorted(list(dp[i])).pop(0)
        return ''


    def test(self):
        testCases = [
            ["w","wo","wor","worl", "world"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ]
        for words in testCases:
            print('words: %s' % words)
            result = self.longestWord(words)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
