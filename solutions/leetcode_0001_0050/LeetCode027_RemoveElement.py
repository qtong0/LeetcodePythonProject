from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
        return j
