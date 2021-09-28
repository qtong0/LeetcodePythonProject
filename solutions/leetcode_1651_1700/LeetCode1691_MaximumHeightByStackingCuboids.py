from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = sorted(sorted(arr) for arr in cuboids)
        n = len(cuboids)
        dp = [0]*n
        res = 0
        for i, (w1, l1, h1) in enumerate(cuboids):
            dp[i] = h1
            for j in range(i):
                w2, l2, h2 = cuboids[j]
                if w1 >= w2 and l1 >= l2 and h1 >= h2:
                    dp[i] = max(dp[i], dp[j]+h1)
            res = max(res, dp[i])
        return res

    def reorder(self, idx, x, y, z):
        if idx == 0:
            return x, y, z
        if idx == 1:
            return z, x, y
        if idx == 2:
            return y, z, x

    def test(self):
        test_cases = [
            [[50,45,20],[95,37,53],[45,23,12]],
            [[38,25,45],[76,35,3]],
            [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]],
        ]
        for cuboids in test_cases:
            res = self.maxHeight(cuboids)
            print('res: %s' % res)


if __name__ == '__main__':
    Solution().test()
