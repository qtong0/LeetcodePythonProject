from typing import List
import bisect, random


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        areas = [(x2-x1+1)*(y2-y1+1) for x1, y1, x2, y2 in rects]
        preSum = 0
        n = len(rects)
        sumArea = sum(areas)
        self.weights = []
        for a in areas:
            preSum += a
            self.weights.append(preSum / sumArea)

    def pick(self) -> List[int]:
        idx = bisect.bisect_left(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
