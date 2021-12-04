from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        graph = [[] for _ in range(61)]
        degrees = [0]*61
        for i in range(1, 61):
            self.search(targetGrid, i, graph, degrees)

        zeros = []
        visited = set()
        for i in range(len(degrees)):
            if degrees[i] == 0:
                zeros.append(i)
                visited.add(i)

        while zeros:
            curr = zeros.pop(0)
            for nei in graph[curr]:
                degrees[nei] -= 1
                if degrees[nei] == 0:
                    zeros.append(nei)
                    visited.add(nei)

        return len(visited) == 61

    def search(self, grid, color, graph, degrees):
        m, n = len(grid), len(grid[0])
        minX, minY, maxX, maxY = float('inf'), float('inf'), float('-inf'), float('-inf')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == color:
                    minX = min(minX, i)
                    minY = min(minY, j)
                    maxX = max(maxX, i)
                    maxY = max(maxY, j)

        if minX == float('inf'):
            return

        for i in range(minX, maxX+1):
            for j in range(minY, maxY+1):
                if grid[i][j] != color:
                    graph[grid[i][j]].append(color)
                    degrees[color] += 1


    def test(self):
        test_cases = [
            [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]],
            [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]],
            [[1,2,1],[2,1,2],[1,2,1]],
            [[1,1,1],[3,1,3]],
        ]
        for targetGrid in test_cases:
            res = self.isPrintable(targetGrid)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
