import bisect


class Solution:
    def maxWidthRamp(self, A: list[int]) -> int:
        n = len(A)
        res = 0
        candidates = [(A[-1], n-1)]
        # candidates: i's decreasing, by increasing value of A[i]
        for i in range(n-2, -1, -1):
            # find largest j in candidateds with A[j] >= A[i]
            jx = bisect.bisect(candidates, (A[i],))
            if jx < len(candidates):
                res = max(res, candidates[jx][1]-i)
            else:
                candidates.append((A[i], i))
        return res
