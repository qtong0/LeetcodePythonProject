class Solution:
    # KMP
    # O(N)
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        dp = [0]*n
        j = 0
        for i in range(1, n):
            if s[i] == s[j]:
                j += 1
                dp[i] = j
            elif j > 0:
                j = dp[j-1]
                i -= 1
        return s[:j]


    def longestPrefix_own(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(1, n):
            pre = s[:i]
            if pre == s[n-i:]:
                res = pre
        return res


    def test(self):
        test_cases = [
            'level',
            'ababab',
            'leetcodeleet',
            'a'
        ]
        for s in test_cases:
            res = self.longestPrefix(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
