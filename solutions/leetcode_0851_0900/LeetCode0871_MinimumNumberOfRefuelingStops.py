import heapq
from typing import List


class Solution(object):
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        h = []
        res = i = 0
        cur = startFuel
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur:
                heapq.heappush(h, -stations[i][1])
                i += 1
            if not h:
                return -1
            cur += -heapq.heappop(h)
            res += 1
        return res
