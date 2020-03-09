class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) < 3:
            return False
        if A[0] > A[1]:
            return False
        i = 1
        while i < len(A) and A[i-1] < A[i]:
            i += 1
        if i == 1 or i == len(A):
            return False
        while i < len(A) and (A[i-1] > A[i]):
            i += 1
        return i == len(A)
