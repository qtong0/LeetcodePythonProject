import heapq


class Solution:
    def kClosest(self, points, K):
        heap = []
        for p in points:
            heapq.heappush(heap, (p[0]**2 + p[1]**2, p))
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
        return res
