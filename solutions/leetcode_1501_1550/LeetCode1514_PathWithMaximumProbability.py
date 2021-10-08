from typing import List
import heapq


class Solution:
    # Dijkstra's Algorithm, Max Heap!
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (n1, n2) in enumerate(edges):
            graph[n1].append([n2, succProb[i]])
            graph[n2].append([n1, succProb[i]])
        visited_prob = [0]*n
        # Max Heap!!!
        heap = [[-1, start]]
        visited_prob[start] = 1

        while heap:
            prob, node = heapq.heappop(heap)
            if node == end:
                return -prob
            for neib, neib_prob in graph[node]:
                if visited_prob[neib] == 0 or visited_prob[neib] < -prob*neib_prob:
                    heapq.heappush(heap, [prob*neib_prob, neib])
                    visited_prob[neib] = -prob*neib_prob
        return visited_prob[end]

    def test(self):
        test_cases = [
            [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2],
            [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2],
            [3, [[0,1]], [0.5], 0, 2],
        ]
        for n, edges, succProb, start, end in test_cases:
            res = self.maxProbability(n, edges, succProb, start, end)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
