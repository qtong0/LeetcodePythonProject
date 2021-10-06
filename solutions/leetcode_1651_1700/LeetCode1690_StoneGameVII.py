from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        pref = [0] * (n+1)
        for i in range(n):
            pref[i+1] = pref[i] + stones[i]

        for gap in range(1, n+1):
            i, j = 0, gap-1
            while j < n:
                if gap == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(
                        pref[j+1] - pref[i+1] - dp[i+1][j],
                        pref[j] - pref[i] - dp[i][j-1]
                    )
                i += 1
                j += 1

        return dp[0][-1]

    def test(self):
        test_cases = [
            [5,3,1,4,2],
            [7,90,5,1,100,10,10,2],
        ]
        for stones in test_cases:
            res = self.stoneGameVII(stones)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
