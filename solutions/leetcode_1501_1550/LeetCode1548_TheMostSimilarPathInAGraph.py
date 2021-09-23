class Solution:
    def mostSimilar(self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]) -> list[int]:
        graph = [[] for _ in range(n)]
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)

        # init variables
        m = len(targetPath)
        dp = [[m]*n for _ in range(m)]
        prev = [[0]*n for _ in range(m)]

        # populate dp
        for v in range(n):
            dp[0][v] = (names[v] != targetPath[0])
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]:
                        dp[i][v] = dp[i-1][u]
                        prev[i][v] = u
                dp[i][v] += (names[v] != targetPath[i])

        # re-construct path
        path, min_dist = [0], m
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
        for i in range(m-1, 0, -1):
            u = prev[i][path[-1]]
            path.append(u)

        return path[::-1]



    # my own solution, DFS, brute force, TLE :(
    def mostSimilar_own_bruteforce_TLE(self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]) -> list[int]:
        name_map = {}
        for i, name in enumerate(names):
            name_map[name] = i
        graph = {}
        for i, j in roads:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append(j)
            graph[j].append(i)
        self.res = []
        self.min_edit = float('inf')
        self.dfs([], names, graph, targetPath, 0)
        return self.res

    def dfs(self, res, names, graph, targetPath, edit):
        if len(res) == len(targetPath):
            if edit < self.min_edit:
                self.min_edit = edit
                self.res = res
        else:
            if not res:
                for i, name in enumerate(names):
                    same = 1 if targetPath[0] != name else 0
                    self.dfs(res + [i], names, graph, targetPath, edit+same)
            else:
                prev = res[-1]
                for i in graph[prev]:
                    same = 1 if targetPath[len(res)] != names[i] else 0
                    self.dfs(res + [i], names, graph, targetPath, edit+same)

    def test(self):
        test_cases = [
            [5, [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], ["ATL","PEK","LAX","DXB","HND"], ["ATL","DXB","HND","LAX"]],
            [4, [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], ["ATL","PEK","LAX","DXB"], ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]],
            [6, [[0,1],[1,2],[2,3],[3,4],[4,5]], ["ATL","PEK","LAX","ATL","DXB","HND"], ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]],
        ]
        for n, roads, names, targetPath in test_cases:
            res = self.mostSimilar(n, roads, names, targetPath)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
