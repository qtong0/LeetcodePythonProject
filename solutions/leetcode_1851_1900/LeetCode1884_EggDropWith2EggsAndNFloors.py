import math


class Solution:
    # Easiest to understand / explain
    # 1. if the egg breaks, the problem is reduced to j-1 eggs and i-1 floors
    # 2. if the eggs does not break, the problem is reduced to j eggs and n-i floors
    #
    def twoEggDrop(self, n: int) -> int:
        eggs = 2
        dp = [[0]*(eggs+1) for _ in range(n+1)]
        return self.drop(n, eggs, dp)

    def drop(self, floors, eggs, dp):
        if eggs == 1 or floors <= 1:
            return floors
        if dp[floors][eggs]:
            return dp[floors][eggs]
        res = float('inf')
        for f in range(1, floors+1):
            res = min(res, 1 + max(self.drop(f-1, eggs-1, dp), self.drop(floors-f, eggs, dp)))
        dp[floors][eggs] = res
        return res



    def twoEggDrop_another_DP(self, n: int) -> int:
        dp = [[0]*3 for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, 3):
                # if egg breaks, then we can check dp[m - 1][k - 1] floors.
                # if egg doesn't breaks, then we can check dp[m - 1][k] floors.
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            if dp[i][j] >= n:
                return i



    # Binary Search solution
    def twoEggDrop_Binary(self, n: int) -> int:
        l, r = 1, n
        res = n
        while l <= r:
            mid = (l+r)//2
            if mid*(mid+1) >= 2*n:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res



    # pure math
    def twoEggDrop_math(self, n: int) -> int:
        return int(math.ceil(math.sqrt(1+8*n)-1)//2)



    def test(self):
        test_cases = [
            2,
            14,
            100,
        ]
        for n in test_cases:
            res = self.twoEggDrop(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
