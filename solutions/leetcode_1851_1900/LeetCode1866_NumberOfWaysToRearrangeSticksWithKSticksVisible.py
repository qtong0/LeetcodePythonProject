class Solution:
    # needs memorization / caching
    def __init__(self):
        self.dp = [[0]*1001 for _ in range(1001)]

    # Insert the shortest stick in front of all the sticks it would be visible
    # So there are k-1 sticks left to insert into n-1 places
    # The above explains
    # self.rearrangeSticks(n-1, k-1)
    #
    # Insert the shortest stick at any position except the beginning, so it would be **invisible**
    # So there are k more sticks left to insert into n-1 places, and there are n-1 ways to do it
    # The above explains
    # self.rearrangeSticks(n-1, k) * (n-1)
    #
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9+7
        if k == n:
            return 1
        if k == 0:
            return 0
        if self.dp[n][k] == 0:
            self.dp[n][k] = (self.rearrangeSticks(n-1, k-1) + self.rearrangeSticks(n-1, k) * (n-1)) % MOD
        return self.dp[n][k]


    def test(self):
        test_cases = [
            [3, 2],
            [5, 5],
            [20, 11],
        ]
        for n, k in test_cases:
            res = self.rearrangeSticks(n, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
