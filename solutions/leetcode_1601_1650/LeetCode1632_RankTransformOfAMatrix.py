import collections
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        self.parent.setdefault(u, u)
        self.parent.setdefault(v, v)
        pu, pv = self.find(u), self.find(v)
        if pu != pv: self.parent[pu] = pv

    def getGroups(self):
        groups = collections.defaultdict(list)
        for i in self.parent.keys():
            groups[self.find(i)].append(i)
        return groups


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        d = collections.defaultdict(list)

        for r in range(m):
            for c in range(n):
                d[matrix[r][c]].append([r, c])

        rank = [0] * (m + n)  # rank[i] is the largest rank of the row or column so far.
        for a in sorted(d):
            uf = UnionFind()

            for r, c in d[a]:
                uf.union(r, c + m)  # Union row `r` with column `c` (column +m to separate with r)

            for group in uf.getGroups().values():
                maxRank = max(rank[i] for i in group)  # Get max rank of all included rows and columns
                for i in group: rank[i] = maxRank + 1  # Update all rows or columns in the same groups to new rank

            for r, c in d[a]:
                matrix[r][c] = rank[r]  # or matrix[r][c] = rank[c+m], both are correct!

        return matrix




class Solution_another:
    # TC: O(NNLog(MN))
    # SC: O(MN)
    #
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        rank = [0] * (m+n)
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[matrix[i][j]].append([i, j])

        def find(i):
            while p[i] != i:
                i = p[i]
            return p[i]

        for a in sorted(d):
            p = list(range(m+n))
            rank2 = list(rank)
            for i, j in d[a]:
                i, j = find(i), find(j+m)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]:
                rank[i] = rank[j+m] = matrix[i][j] = rank2[find(i)] + 1

        return matrix


    def test(self):
        test_cases = [
            [[1,2],[3,4]],
            [[7,7],[7,7]],
            [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]],
            [[7,3,6],[1,4,5],[9,8,2]],
        ]
        for matrix in test_cases:
            res = self.matrixRankTransform(matrix)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution_another().test()
