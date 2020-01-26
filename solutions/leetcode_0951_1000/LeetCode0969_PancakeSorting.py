class Solution:
    def pancakeSort(self, A):
        res = []
        n = len(A)
        nums = sorted(range(1, n+1), key = lambda i: -A[i-1])
        for i in nums:
            for f in res:
                if i <= f:
                    i = f+1-i
            res += [i, n]
            n -= 1
        return res
