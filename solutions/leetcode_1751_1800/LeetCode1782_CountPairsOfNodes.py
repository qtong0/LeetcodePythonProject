from collections import Counter
from typing import List


class Solution:
    # TC: O(q(n + e)) w/ sorting O(N(Log(N))
    # Memory O(n + e)
    # q - queries, n - nodes, e - edges
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        count = [0] * (n+1)
        res = [0] * (len(queries))
        shared = Counter((min(n1, n2), max(n1, n2)) for n1, n2 in edges)
        for n1, n2 in edges:
            count[n1] += 1
            count[n2] += 1
        sorted_count = sorted(count)
        for k, q in enumerate(queries):
            i, j = 1, n
            while i < j:
                if q < sorted_count[i] + sorted_count[j]:
                    res[k] += j-i
                    j -= 1
                else:
                    i += 1
            for (i, j), shared_count in shared.items():
                if q < count[i] + count[j] <= q + shared_count:
                    res[k] -= 1
        return res

    def test(self):
        test_cases = [
            [4, [[1,2],[2,4],[1,3],[2,3],[2,1]], [2,3]],
            [5, [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], [1,2,3,4,5]],
            [
                6,
                [[5,2],[3,5],[4,5],[1,5],[1,4],[3,5],[2,6],[6,4],[5,6],[4,6],[6,2],[2,6],[5,4],[6,1],[6,1],[2,5],[1,3],[1,3],[4,5]],
                [6,9,2,1,2,3,6,6,6,5,9,7,0,4,5,9,1,18,8,9],
            ],
        ]
        for n, edges, queries in test_cases:
            res = self.countPairs(n, edges, queries)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
