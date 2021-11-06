import math, collections


class Solution:
    def numSquarefulPerms(self, A) -> int:
        counter = {}
        for num in A:
            counter[num] = counter.get(num, 0) + 1
        cand = {i: {j for j in counter if int((i + j)**0.5) ** 2 == i + j} for i in counter}
        self.res = 0
        for x in counter:
            self.dfs(counter, cand, x, len(A)-1)
        return self.res

    def dfs(self, counter, cand, x, left):
        counter[x] -= 1
        if left == 0:
            self.res += 1
        for y in cand[x]:
            if counter[y]:
                self.dfs(counter, cand, y, left-1)
        counter[x] += 1


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
            [2,2,2],
            [2,2,2,2,2,2,2,2,2,2],
        ]
        for arr in testCases:
            res = self.numSquarefulPerms(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
