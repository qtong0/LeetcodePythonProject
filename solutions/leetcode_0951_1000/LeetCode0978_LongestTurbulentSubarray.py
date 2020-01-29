class Solution:
    def maxTurbulenceSize(self, A) -> int:
        odd, even = 1, 1
        res = 1
        for i in range(1, len(A)):
            if i % 2 == 0:
                if A[i-1] > A[i]:
                    even += 1
                    res = max(res, odd, even)
                    odd = 1
                elif A[i-1] < A[i]:
                    odd += 1
                    res = max(res, odd, even)
                    even = 1
                else:
                    res = max(res, odd, even)
                    odd = 1
                    even = 1
            else:
                if A[i-1] > A[i]:
                    odd += 1
                    res = max(res, odd, even)
                    even = 1
                elif A[i-1] < A[i]:
                    even += 1
                    res = max(res, odd, even)
                    odd = 1
                else:
                    res = max(res, odd, even)
                    odd = 1
                    even = 1
        return res

    def test(self):
        testCases = [
            [9,4,2,10,7,8,8,1,9],
            [4,8,12,16],
            [10],
        ]
        for arr in testCases:
            res = self.maxTurbulenceSize(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
