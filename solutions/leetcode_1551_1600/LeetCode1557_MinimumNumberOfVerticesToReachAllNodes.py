from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        degree = [0]*n
        for e1, e2 in edges:
            graph[e1].append(e2)
            degree[e2] += 1
        res = []
        for e in range(n):
            if degree[e] == 0:
                res.append(e)
        return res

    def test(self):
        test_cases = [
            [6, [[0,1],[0,2],[2,5],[3,4],[4,2]]],
            [5, [[0,1],[2,1],[3,1],[1,4],[2,4]]],
        ]
        for n, edges in test_cases:
            res = self.findSmallestSetOfVertices(n, edges)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
