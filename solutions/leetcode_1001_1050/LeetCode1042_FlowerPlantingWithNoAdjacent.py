from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {}
        for n1, n2 in paths:
            graph[n1-1] = graph.get(n1-1, []) + [n2-1]
            graph[n2-1] = graph.get(n2-1, []) + [n1-1]
        res = [0]*n
        for i in range(n):
            colors = [0]*5
            for j in graph.get(i, []):
                colors[res[j]] = 1
            for c in range(1, 5):
                if colors[c] == 0:
                    res[i] = c
        return res



    def test(self):
        test_cases = [
            [1, []],
            [3, [[1,2],[2,3],[3,1]]],
            [4, [[1,2],[3,4]]],
            [4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]],
        ]
        for n, paths in test_cases:
            res = self.gardenNoAdj(n, paths)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
