class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(A) and A[i-1] < A[i]:
            i += 1
        if i == 0:
            return False
        while i < len(A) and A[i-1] > A[i]:
            i += 1
