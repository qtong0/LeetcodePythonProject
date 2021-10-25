from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res, curr = 0, 0
        for g in gain:
            curr += g
            res = max(res, curr)
        return res
