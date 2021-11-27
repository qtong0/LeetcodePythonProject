from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        m = max(len(w) for w in words)
        if not words or len(words[0]) != 1:
            return ''
        dp = [set() for _ in range(m+1)]
        maxLen = 0
        for w in words:
            if len(w) == 1:
                dp[len(w)].add(w)
            else:
                if w[:-1] in dp[len(w)-1]:
                    dp[len(w)].add(w)
            if dp[len(w)]:
                maxLen = max(maxLen, len(w))
        if dp[maxLen]:
            return sorted(dp[maxLen])[0]
        else:
            return ''


    def test(self):
        test_cases = [
            ["k","ki","kir","kira", "kiran"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"],
            ["abc", "bc", "ab", "qwe"],
        ]
        for words in test_cases:
            res = self.longestWord(words)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
