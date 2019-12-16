class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        left  = [float('-inf')]*n
        left[0] = A[0]
        for i in range(1, n):
            left[i] = max(left[i-1], A[i])
        right = [float('inf')]*n
        right[-1] = A[-1]
        for i in range(n-2, -1, -1):
            right[i] = min(right[i+1], A[i])
        for i in range(n-1):
            if left[i] <= right[i+1]:
                return i+1
        return -1

    def test(self):
        testCases = [
            [1,1],
            [5,0,3,8,6],
            [1,1,1,0,6,12],
        ]
        for arr in testCases:
            res = self.partitionDisjoint(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
