from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i, num in enumerate(self.nums):
            if target == num:
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res
