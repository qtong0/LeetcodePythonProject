class Solution:
    def treeDiameter(self, edges) -> int:
        self.diameter = 0
        def dfs(node, pre):
            d1 = d2 = 0
            for neighbor in graph[node]:
                if neighbor != pre:
                    d = dfs(neighbor, node)
                    if d > d1:
                        d1, d2 = d, d1
                    elif d > d2:
                        d2 = d
            self.diameter = max(self.diameter, d1+d2)
            return d1+1
        graph = {}
        for e in edges:
            if e[0] not in graph:
                graph[e[0]] = []
            graph[e[0]].append(e[1])
            if e[1] not in graph:
                graph[e[1]] = []
            graph[e[1]].append(e[0])
        dfs(0, None)
        return self.diameter

    # Down solution is TLE
    def treeDiameter_own_TLE(self, edges) -> int:
        graph = {}
        degree = {}
        for e in edges:
            if e[0] not in graph:
                graph[e[0]] = set()
            graph[e[0]].add(e[1])
            if e[1] not in graph:
                graph[e[1]] = set()
            graph[e[1]].add(e[0])
            degree[e[0]] = degree.get(e[0], 0)+1
            degree[e[1]] = degree.get(e[1], 0)+1
        nodes = []
        for node, d in degree.items():
            if d == 1:
                nodes.append(node)
        self.maxLen = 0
        for node in nodes:
            visited = set([node])
            self.dfs(node, 0, visited, graph)
        return self.maxLen

    def dfs(self, node, length, visited, graph):
        self.maxLen = max(self.maxLen, length)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, length+1, visited, graph)

    def test(self):
        testCases = [
            [[0,1],[0,2]],
            [[0,1],[1,2],[2,3],[1,4],[4,5]],
        ]
        for edges in testCases:
            res = self.treeDiameter(edges)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
