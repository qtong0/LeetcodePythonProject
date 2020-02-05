import math


class Solution:
    # this solution is TLE only
    # needs to check later to get best solution
    def numSquarefulPerms(self, A) -> int:
        res = set()
        self.helper(res, [], A, len(A))
        return len(res)

    def helper(self, res, arr, curr, n):
        if len(arr) == n:
            res.add(str(arr))
        for i, num in enumerate(curr):
            if not arr or self.isSquare(arr[-1]+num):
                self.helper(res, arr+[num], curr[:i]+curr[i+1:], n)

    def isSquare(self, num):
        val = math.sqrt(num)
        return int(val) == val

    def test(self):
        testCases = [
            [1,17,8],
            # [2,2,2],
            [2,2,2,2,2,2,2,2,2,2],
        ]
        for arr in testCases:
            res = self.numSquarefulPerms(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
