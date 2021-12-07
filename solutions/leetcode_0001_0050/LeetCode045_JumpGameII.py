from typing import List


class Solution(object):
    def jump(self, nums: List[int]) -> int:
        maxReach = 0
        reach = 0
        steps = 0
        for i in range(len(nums)-1):
            maxReach = max(maxReach, i+nums[i])
            if i == reach:
                steps += 1
                reach = maxReach
        return steps
