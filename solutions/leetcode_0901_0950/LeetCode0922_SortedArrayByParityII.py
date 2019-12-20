class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while j < len(A):
            while i < len(A) and A[i] % 2 == 0:
                i += 2
            while j < len(A) and A[j] % 2 == 1:
                j += 2
            if i < len(A) and j < len(A):
                A[i], A[j] = A[j], A[i]
            i += 2
            j += 2
        return A

    def test(self):
        testCases = [
            [4, 2, 5, 7],
            [3,1,4,2],
        ]
        for arr in testCases:
            res = self.sortArrayByParityII(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
