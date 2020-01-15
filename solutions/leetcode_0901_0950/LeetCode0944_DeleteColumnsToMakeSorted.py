class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        res = 0
        for j in range(n):
            for i in range(m):
                if i > 0:
                    if A[i][j] <= A[i-1][j]:
                        res += 1
                        break
        return res
