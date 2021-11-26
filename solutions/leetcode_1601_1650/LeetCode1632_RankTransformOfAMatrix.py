import collections
from typing import List


class Solution:
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
    Solution().test()
