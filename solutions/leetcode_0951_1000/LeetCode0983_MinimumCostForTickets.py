class Solution:
    def mincostTickets(self, days, costs) -> int:
        if not days or not costs: return 0
        n = len(days)
        lastDay = days[n-1]
        dp = [0]*(lastDay+1)

        daysSet = set(days)

        for i in range(1, lastDay+1):
            if i not in daysSet:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0],
                            dp[max(i-7, 0)] + costs[1],
                            dp[max(i-30, 0)] + costs[2])
        return dp[-1]

    def test(self):
        testCases = [
            [
                [4,5,9,11,14,16,17,19,21,22,24],
                [1,4,18],
            ],  # 11
            [
                [1,4,6,7,8,20],
                [2,7,15],
            ],  # 11
            [
                [1,2,3,4,5,6,7,8,9,10,30,31],
                [2,7,15],
            ],  # 17
        ]
        for days, costs in testCases:
            res = self.mincostTickets(days, costs)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
