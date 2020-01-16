class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        A.sort()
        s, res = A[0], 0
        for num in A:
            res += max(0, s-num)
            s = max(s+1, num+1)
        return res

    def test(self):
        testCases = [
            # [1,2,2],
            # [3,2,1,2,1,7],
            [7,2,7,2,1,4,3,1,4,8],
        ]
        for arr in testCases:
            res = self.minIncrementForUnique(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
