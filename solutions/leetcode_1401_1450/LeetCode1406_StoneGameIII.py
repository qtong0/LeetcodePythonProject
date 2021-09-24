class Solution:
    # Best solution, O(1) space complexity
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0]*4
        for i in range(n-1, -1, -1):
            dp[i % 4] = float('-inf')
            take = 0
            for k in range(3):
                if i+k < n:
                    take += stoneValue[i+k]
                    dp[i % 4] = max(dp[i % 4], take-dp[(i+k+1) % 4])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'

    # O(n) space complexity, easier to understand
    def stoneGameIII_More_Space(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n+1)
        dp[-1] = 0
        for i in range(n-1, -1, -1):
            take = 0
            for k in range(3):
                if i+k < n:
                    take += stoneValue[i+k]
                    dp[i] = max(dp[i], take-dp[i+k+1])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'

    def test(self):
        test_cases = [
            [1,2,3,7],
            [1,2,3,-9],
            [1,2,3,6],
            [1,2,3,-1,-2,-3,7],
            [-1,-2,-3],
        ]
        for stoneValue in test_cases:
            res = self.stoneGameIII(stoneValue)
            res_space = self.stoneGameIII_More_Space(stoneValue)
            print('res: %s' % res)
            print('res_space: %s' % res_space)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
