from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i, j = n-1, 2*n-1
        while i >= 0:
            res.insert(0, nums[j])
            res.insert(0, nums[i])
            j -= 1
            i -= 1
        return res
