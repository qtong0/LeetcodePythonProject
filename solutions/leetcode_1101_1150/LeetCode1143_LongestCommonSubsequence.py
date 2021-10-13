class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0]*(n+1)
        for i in range(m):
            new_dp = [0]*(n+1)
            for j in range(n):
                if text1[i] == text2[j]:
                    new_dp[j+1] = dp[j] + 1
                else:
                    new_dp[j+1] = max(dp[j], dp[j+1], new_dp[j])
            dp = new_dp
        return dp[-1]

    # own solution
    def longestCommonSubsequence_own_space(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]

    def test(self):
        test_cases = [
            ['abcde', 'ace'],
            ['abc', 'abc'],
            ['abc', 'def'],
            ["abcba", "abcbcba"],
        ]
        for s1, s2 in test_cases:
            res_1 = self.longestCommonSubsequence(s1, s2)
            res_2 = self.longestCommonSubsequence_own_space(s1, s2)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
