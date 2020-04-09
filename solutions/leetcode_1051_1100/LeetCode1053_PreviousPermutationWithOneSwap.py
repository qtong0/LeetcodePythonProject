class Solution:
    def prevPermOpt1(self, A):
        left = len(A)-2
        while left >= 0:
            if A[left] > A[left+1]:
                break
            left -= 1
        if left == -1:
            return A
        right = len(A)-1
        while A[right] >= A[left]:
            right -= 1
        rightVal = A[right]
        while A[right] == rightVal:
            right -= 1
        right += 1
        A[left], A[right] = A[right], A[left]
        return A


    def prevPermOpt1_own_wrong(self, A):
        n = len(A)
        i = n-1
        while i >= 0:
            while i > 0 and A[i-1] == A[i]:
                i -= 1
            for j in range(i-1, -1, -1):
                if A[j] > A[i]:
                    A[i], A[j] = A[j], A[i]
                    return A
            i -= 1
        return A


    def test(self):
        testCases = [
            # [3,1,1,3],
            # [3,2,1],
            # [1,1,5],
            [1,9,4,6,7],
        ]
        for arr in testCases:
            res = self.prevPermOpt1(arr)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
