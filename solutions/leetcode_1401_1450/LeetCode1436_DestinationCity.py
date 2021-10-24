from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        degrees = {}
        graph = {}
        for c1, c2 in paths:
            if c1 not in degrees:
                degrees[c1] = 0
            degrees[c2] = degrees.get(c2, 0) + 1
            graph[c1] = c2
        start = ''
        for c, degree in degrees.items():
            if degree == 0:
                start = c
                break
        while start in graph:
            start = graph[start]
        return start

    def test(self):
        test_cases = [
            [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]],
            [["B","C"],["D","B"],["C","A"]],
            [["A","Z"]],
        ]
        for paths in test_cases:
            res = self.destCity(paths)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
