import functools


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        @functools.lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            return max(dp(i+1, s),
                       dp(i+1, s-rods[i]),
                       dp(i+1, s+rods[i]) + rods[i])
        return dp(0, 0)

    def test(self):
        testCases = [
            [1,2,3,6],
            [1,2,3,4,5,6],
            [1,2],
        ]
        for rods in testCases:
            res = self.tallestBillboard(rods)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
