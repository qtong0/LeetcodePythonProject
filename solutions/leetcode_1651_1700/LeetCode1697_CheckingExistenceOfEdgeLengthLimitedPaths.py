from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        pr, qr = self.find(p), self.find(q)
        if pr == qr:
            return False
        if self.rank[pr] > self.rank[qr]:
            pr, qr = qr, pr
        self.parent[pr] = qr
        self.rank[qr] += self.rank[pr]
        return True


class Solution:
    # Union Find!
    # TC: O(NlogN) + O(MlogM)
    # SC: O(N)
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, n1, n2) for n1, n2, w in edgeList)

        union_find = UnionFind(n)

        res = [None] * len(queries)
        idx = 0
        for w, p, q, i in queries:
            while idx < len(edgeList) and edgeList[idx][0] < w:
                _, n1, n2 = edgeList[idx]
                union_find.union(n1, n2)
                idx += 1
            res[i] = union_find.find(p) == union_find.find(q)
        return res




    # Own BFS solution - TLE
    def distanceLimitedPathsExist_own_TLE(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [{} for _ in range(n)]
        for n1, n2, w in edgeList:
            if n2 not in graph[n1]:
                graph[n1][n2] = w
            else:
                graph[n1][n2] = min(w, graph[n1][n2])
            if n1 not in graph[n2]:
                graph[n2][n1] = w
            else:
                graph[n2][n1] = min(w, graph[n2][n1])
        res = []
        for n1, n2, threshold in queries:
            res.append(self.bfs(graph, n1, n2, threshold))
        return res

    def bfs(self, graph, n1, n2, threshold):
        queue = [n1]
        visited = set([n1])
        while queue:
            n = queue.pop(0)
            if n == n2:
                return True
            for nei, w in graph[n].items():
                if w < threshold and nei not in visited:
                    queue.append(nei)
                    visited.add(nei)
        return False

    def test(self):
        test_cases = [
            [3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]]],
            [5, [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], [[0,4,14],[1,4,13]]],
        ]
        for n, edge_list, queries in test_cases:
            res = self.distanceLimitedPathsExist(n, edge_list, queries)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
