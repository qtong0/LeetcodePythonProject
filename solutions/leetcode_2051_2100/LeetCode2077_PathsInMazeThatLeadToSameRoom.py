from collections import defaultdict
from typing import List


class Solution:
    # Greedy
    # O(V*E)
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        res = 0
        neigbors = defaultdict(set)
        for firstNode, thirdNode in corridors:
            neigbors[thirdNode].add(firstNode)
            neigbors[firstNode].add(thirdNode)
            res += len(neigbors[firstNode].intersection(neigbors[thirdNode]))
        return res



    # Own TLE DFS Solution :(
    def numberOfPaths_own_TLE(self, n: int, corridors: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        for n1, n2 in corridors:
            graph[n1].append(n2)
            graph[n2].append(n1)
        self.cand = set()
        for node in range(1, n+1):
            visited = [False]*(n+1)
            self.dfs(graph, node, [node], visited)
        return len(self.cand)

    def dfs(self, graph, node, curr, visited):
        visited[node] = True
        if len(curr) > 3:
            return
        for nei in graph[node]:
            if nei == curr[0] and len(curr) == 3:
                self.cand.add(str(sorted(curr)))
            elif nei not in visited:
                self.dfs(graph, nei, curr + [nei], visited)



    def test(self):
        test_cases = [
            [5, [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]],
            [4, [[1,2],[3,4]]],
            [5, [[4,1],[4,2],[3,4],[5,3],[5,2],[1,3],[3,2],[2,1],[5,4],[5,1]]],
        ]
        for n, corridors in test_cases:
            res = self.numberOfPaths(n, corridors)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
