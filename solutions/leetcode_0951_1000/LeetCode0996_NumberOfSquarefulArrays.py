import math, collections


class Solution:
    def numSquarefulPerms(self, A) -> int:
        c = collections.Counter(A)
        cand = {i: {j for j in c if int((i + j)**0.5) ** 2 == i + j} for i in c}
        self.res = 0
        def dfs(x, left=len(A) - 1):
            c[x] -= 1
            if left == 0: self.res += 1
            for y in cand[x]:
                if c[y]: dfs(y, left - 1)
            c[x] += 1
        for x in c: dfs(x)
        return self.res


    # this solution is TLE only
    # needs to check later to get best solution
    def numSquarefulPerms_own_TLE(self, A) -> int:
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
