from typing import List


class Solution(object):
    # dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
    # You can first pick piles[i] or piles[j].
    #
    # If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
    # If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
    # So we get:
    # dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    #
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n-d):
                dp[i][i+d] = max(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])
        return dp[0][-1] > 0
    
    def test(self):
        testCases = [
            [3,7,2,3],
            [5,3,4,5],
        ]
        for piles in testCases:
            res = self.stoneGame(piles)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
