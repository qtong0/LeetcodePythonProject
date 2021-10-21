from typing import List


class Solution(object):
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        include, exclude = 0, 0
        for num in nums:
            i, e = include, exclude
            include = e+num
            exclude = max(i, e)
        return max(include, exclude)
