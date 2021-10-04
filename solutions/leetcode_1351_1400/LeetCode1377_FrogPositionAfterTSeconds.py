from typing import List


class Solution:
    # My own BFS solution
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for _ in range(n+1)]
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        # [node, pos, time]
        queue = [[1, 1, 0]]
        # [pos, time]
        pos_map = [[] for _ in range(n+1)]
        pos_map[1] = [1, 0]

        while queue:
            node, pos, time = queue.pop(0)
            if node == target and time == t:
                return pos
            eligible_nodes = []
            for e in graph[node]:
                if not pos_map[e]:
                    eligible_nodes.append(e)
            if eligible_nodes:
                pos_map[node] = [0, time]
                next_pos = pos / len(eligible_nodes)
                for e in eligible_nodes:
                    queue.append([e, next_pos, time+1])
                    pos_map[e] = [next_pos, time+1]

        if pos_map[target] and pos_map[target][1] <= t:
            return pos_map[target][0]
        else:
            return 0

    # another DFS solution
    def frogPosition_dfs(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1: return 1.0
        graph = [[] for _ in range(n+1)]
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        visited = [False]*(n+1)

        return self.dfs(graph, 1, t, target, visited)

    def dfs(self, graph, node, t, target, visited):
        if (node != 1 and len(graph[node]) == 1) or t == 0:
            if node == target:
                return 1
            else:
                return 0
        visited[node] = True
        res = 0.0
        for e in graph[node]:
            if not visited[e]:
                res += self.dfs(graph, e, t-1, target, visited)
        if node != 1:
            return res * 1.0 / (len(graph[node]) - 1)
        else:
            return res * 1.0 / len(graph[node])

    def test(self):
        test_cases = [
            [3, [[2,1],[3,2]], 1, 2],
            [7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4],
            [7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7],
            [7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6],
            [8, [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]], 7, 7],
        ]
        for n, edges, t, target in test_cases:
            res_1 = self.frogPosition(n, edges, t, target)
            res_2 = self.frogPosition_dfs(n, edges, t, target)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
