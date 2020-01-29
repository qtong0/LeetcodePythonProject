class Solution:
    def sortedSquares(self, A):
        i, j = 0, len(A)-1
        res = []
        while i <= j:
            if A[i]**2 >= A[j]**2:
                res.insert(0, A[i]**2)
                i += 1
            else:
                res.insert(0, A[j]**2)
                j -= 1
        return res

    def sortedSquares_own(self, A):
        l, r = 0, len(A)-1
        while l <= r:
            mid = (l+r)//2
            if A[mid] >= 0:
                r = mid-1
            else:
                l = mid+1
        i = r+1
        l, r = 0, len(A)-1
        while l <= r:
            mid = (l+r)//2
            if A[mid] > 0:
                r = mid-1
            else:
                l = mid+1
        j = r+1
        res = [0]*(j-i)
        i -= 1
        while i >= 0 or j < len(A):
            if i >= 0 and j < len(A):
                if A[i]**2 < A[j]**2:
                    res.append(A[i]**2)
                    i -= 1
                else:
                    res.append(A[j]**2)
                    j += 1
            else:
                if i >= 0:
                    res.append(A[i]**2)
                    i -= 1
                else:
                    res.append(A[j]**2)
                    j += 1
        return res

    def test(self):
        testCases = [
            [-4,-1,0,3,10],
            [-7,-3,2,3,11],
            [-1,0,0,0],
            [-2,-1,-1,-1],
        ]
        for arr in testCases:
            res = self.sortedSquares(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
