class Solution:
    # DFS + Memorization is easier to understand
    def minInsertions(self, s: str) -> int:
        n = len(s)
        memo = [[-1]*n for _ in range(n)]
        return self.helper(s, 0, n-1, memo)

    def helper(self, s, i, j, memo):
        if i >= j:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if s[i] == s[j]:
            res = self.helper(s, i+1, j-1, memo)
        else:
            res = min(self.helper(s, i+1, j, memo), self.helper(s, i, j-1, memo)) + 1
        memo[i][j] = res
        return res

    # DP only
    def minInsertions_another(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[n-1-j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return n - dp[n][n]


    def test(self):
        test_cases = [
            'zzazz',
            'mbadm',
            'leetcode',
            'g',
            'no',
        ]
        for s in test_cases:
            res_1 = self.minInsertions(s)
            res_2 = self.minInsertions_another(s)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
