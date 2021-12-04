from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for c1, c2 in connections:
            graph[c1].append(c2)
            graph[c2].append(-c1)
        visited = [False]*n
        visited[0] = True
        return self.dfs(graph, visited, 0)

    def dfs(self, graph, visited, node):
        change = 0
        visited[node] = True
        for nei in graph[node]:
            if not visited[abs(nei)]:
                change += self.dfs(graph, visited, abs(nei))
                if nei > 0:
                    change += 1
        return change


    def test(self):
        test_cases = [
            [6, [[0,1],[1,3],[2,3],[4,0],[4,5]]],
            [5, [[1,0],[1,2],[3,2],[3,4]]],
            [3, [[1,0],[2,0]]],
        ]
        for n, connections in test_cases:
            res = self.minReorder(n, connections)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
