class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        prev = [0]*n
        for i in range(n):
            curr = [0]*n
            for j in range(n):
                minVal = prev[j] + A[i][j]
                if j > 0:
                    minVal = min(minVal, prev[j-1] + A[i][j])
                if j+1 < n:
                    minVal = min(minVal, prev[j+1] + A[i][j])
                curr[j] = minVal
            prev = curr
        return min(prev)

    def test(self):
        testCases = [
            [
                [-19,57],
                [-40,-5]
            ],
            [
                [1,2,3],
                [4,5,6],
                [7,8,9],
            ],
        ]
        for m in testCases:
            res = self.minFallingPathSum(m)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
