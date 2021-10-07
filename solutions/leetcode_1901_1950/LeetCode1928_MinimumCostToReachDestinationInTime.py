from typing import List
import heapq


class Solution:
    # Dijkstra's Algorithm
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for n1, n2, t in edges:
            graph[n1].append([n2, t])
            graph[n2].append([n1, t])

        visited_times = {}
        # fee, node, time
        heap = [[passingFees[0], 0, 0]]

        while heap:
            fee, node, t = heapq.heappop(heap)

            if t > maxTime:
                continue
            if node == n-1:
                return fee

            if node not in visited_times or visited_times[node] > t:
                visited_times[node] = t
                for next_node, trip_time in graph[node]:
                    heapq.heappush(heap, [fee+passingFees[next_node], next_node, t + trip_time])

        return -1

    def test(self):
        test_cases = [
            [30, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]],
            [29, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]],
            [25, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]],
        ]
        for maxTime, edges, passingFees in test_cases:
            res = self.minCost(maxTime, edges, passingFees)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
