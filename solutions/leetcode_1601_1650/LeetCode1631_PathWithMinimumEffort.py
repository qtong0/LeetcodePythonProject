from typing import List
import heapq


class Solution:
    # Dijkstra's Algorithm
    # keep track of visited - minimum of max distances
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap = [[0, 0, 0]]
        visited = [[float('inf')]*n for _ in range(m)]

        while heap:
            d, i, j = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return d
            for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                if 0 <= x < m and 0 <= y < n:
                    d1 = abs(heights[x][y] - heights[i][j])
                    max_d = max(d, d1)
                    if max_d < visited[x][y]:
                        heapq.heappush(heap, [max_d, x, y])
                        visited[x][y] = max_d

    def test(self):
        test_cases = [
            [[1,2,2],[3,8,2],[5,3,5]],
            [[1,2,3],[3,8,4],[5,3,5]],
            [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
        ]
        for heights in test_cases:
            res = self.minimumEffortPath(heights)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
