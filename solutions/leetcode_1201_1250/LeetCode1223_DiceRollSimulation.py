from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0]*7 for _ in range(n+1)]
        dp[0][6] = 1
        for j in range(6):
            dp[1][j] = 1
        dp[1][6] = 6

        # roll the dice from 2 times, until n times
        for i in range(2, n+1):
            # iterate through each column (face)
            for j in range(6):
                # at each [i, j], trying to go up (decrease i) and collect all the sum of previous state
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i-k][6] - dp[i-k][j]
            # update total sum of this row
            dp[i][6] = sum(dp[i])
        return dp[-1][6] % (10**9+7)

    def test(self):
        test_cases = [
            [2, [1,1,2,2,2,3]],
            [2, [1,1,1,1,1,1]],
            [3, [1,1,1,2,2,3]],
        ]
        for n, rollMax in test_cases:
            res = self.dieSimulator(n, rollMax)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
