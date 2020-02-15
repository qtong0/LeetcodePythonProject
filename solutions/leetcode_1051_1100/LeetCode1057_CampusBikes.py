import heapq
import collections


class Solution:
    def assignBikes(self, workers, bikes):
        dist_map = collections.defaultdict(list)

        m, n = len(workers), len(bikes)
        for i in range(m):
            for j in range(n):
                w = workers[i]
                b = bikes[j]
                dist = abs(w[0]-b[0]) + abs(w[1]-b[1])
                heap = dist_map[dist]
                heapq.heappush(heap, (i, j))
                dist_map[dist] = heap

        assigned_workers = set()
        assigned_bikes = set()
        res = [0]*m
        distances = sorted(list(dist_map.keys()))

        for d in distances:
            heap = dist_map[d]
            while heap:
                pair = heapq.heappop(heap)
                if pair[0] not in assigned_workers and pair[1] not in assigned_bikes:
                    res[pair[0]] = pair[1]
                    assigned_workers.add(pair[0])
                    assigned_bikes.add(pair[1])

        return res
