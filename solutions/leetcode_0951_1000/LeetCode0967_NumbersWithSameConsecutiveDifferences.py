class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = []
        for i in range(10):
            curr = [i]
            self.dfs(res, curr, N, K)
        ans = []
        for arr in res:
            if len(arr) <= 1 or arr[0] != 0:
                ans.append(int(''.join([str(c) for c in arr])))
        return ans

    def dfs(self, res, curr, N, K):
        if len(curr) == N:
            res.append(list(curr))
            return
        for num in range(10):
            if abs(num-curr[-1]) == K:
                self.dfs(res, curr+[num], N, K)

    def test(self):
        testCases = [
            [1, 0],
            [3, 7],
            [2, 1],
        ]
        for n, k in testCases:
            res = self.numsSameConsecDiff(n, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
