class Solution:
    def pancakeSort(self, A):
        res = []
        n = len(A)
        arr = sorted(range(1, n+1), key = lambda i: -A[i-1])
        for i in arr:
            for j in res:
                if i <= j:
                    i = j+1 - i
            res.extend([i, n])
            n -= 1
        return res

    def test(self):
        testCases = [
            [3,2,4,1],
            [1,2,3],
        ]
        for arr in testCases:
            res = self.pancakeSort(arr)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
