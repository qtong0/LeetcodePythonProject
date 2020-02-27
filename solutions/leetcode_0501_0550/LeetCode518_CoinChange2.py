class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(amount):
                if i+c < amount+1:
                    dp[i+c] += dp[i]
        return dp[-1]

    def test(self):
        testCases = [
            [5, [1,2,5]],
            [3, [2]],
            [10, [10]],
        ]
        for amount, coins in testCases:
            res = self.change(amount, coins)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
