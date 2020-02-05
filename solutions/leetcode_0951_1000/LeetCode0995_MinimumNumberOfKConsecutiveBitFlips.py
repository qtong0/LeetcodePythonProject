class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        n = len(A)
        # Tell when to close an interval
        needClose = [0]*n
        res = 0
        nIntervals = 0
        for i, num in enumerate(A):
            # Close this interval if needed
            if needClose[i]:
                nIntervals -= 1
            # When meet following two situations, we need flipping here
            # if A[i] is 0 and number of intervals is even
            # --> means the flippings are totally cancelled. We need another flip
            # if A[i] is 1 and number of intervals is odd
            # --> means we have 1 before but being flipped to 0. Need flip again.
            if (not A[i] and nIntervals % 2 ==0) or \
                    (A[i] and nIntervals % 2 == 1):
                # Need flip again. Update answer count
                res += 1
                # Generate an interval
                nIntervals += 1
                if i+K > n:
                    # A[n-K] is the final possible flipping position
                    # i > n-K means we need to flip the subarray is less than K elements
                    # impossible!
                    return -1
                # Update needClose, so the current interval will be closed at A[i+K]
                if i+K < n:
                    needClose[i+K] = True
        return res
