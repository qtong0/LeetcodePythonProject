class Solution:
    def largestPerimeter(self, A) -> int:
        A.sort()
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

    def test(self):
        testCases = [
            [2,1,2],
            [1,2,1],
            [3,2,3,4],
            [3,6,2,3],
        ]
        for arr in testCases:
            res = self.largestPerimeter(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
