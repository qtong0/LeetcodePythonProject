class Solution(object):
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = {}
        for u, v in dislikes:
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        colors = {}
        for node in range(1, N+1):
            if node not in colors:
                if not self.dfs(colors, graph, node, 0):
                    return False
        return True

    def dfs(self, colors, graph, node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        if node in graph:
            for nei in graph[node]:
                if not self.dfs(colors, graph, nei, 1-color):
                    return False
        return True


    def test(self):
        testCases = [
            [
                1,
                [],
            ],
            [
                4,
                [[1, 2], [1, 3], [2, 4]],
            ],
            [
                3,
                [[1,2],[1,3],[2,3]],
            ],
        ]
        for N, dislikes in testCases:
            res = self.possibleBipartition(N, dislikes)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
