from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, 0]]

        # d1, d2: row, col number to count of lamp
        # d3, d4: diagonal x-y, x+y count of lamp
        # d5: count of lamps for location n * x + y
        d1, d2, d3, d4, d5 = {}, {}, {}, {}, {}
        for x, y in lamps:
            d1[x] = d1.get(x, 0) + 1
            d2[y] = d2.get(y, 0) + 1
            d3[x-y] = d3.get(x-y, 0) + 1
            d4[x+y] = d4.get(x+y, 0) + 1
            d5[n * x + y] = d5.get(n * x + y, 0) + 1

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            ans[i] = 1 if (d1.get(x, 0) > 0 or d2.get(y, 0) > 0 or d3.get(x-y, 0) > 0 or d4.get(x+y, 0) > 0) else 0
            for d in dirs:
                x1, y1 = x + d[0], y + d[1]
                if 0 <= x1 < n and 0 <= y1 < n and n * x1 + y1 in d5:
                    # turn off the light, decrement the counts
                    times = d5.get(n * x1 + y1)
                    d1[x1] = d1.get(x1, 1) - times
                    d2[y1] = d2.get(y1, 1) - times
                    d3[x1 - y1] = d3.get(x1 - y1, 1) - times
                    d4[x1 + y1] = d4.get(x1 + y1, 1) - times
                    del d5[n * x1 + y1]
        return ans

    def test(self):
        testcases = [
            [5, [[0, 0], [0,4]], [[0,4],[0,1],[1,4]]],
            [6, [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]], [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]],
            [1, [[0,0],[0,0]], [[0,0],[0,0]]],
        ]
        for n, lamps, queries in testcases:
            res = self.gridIllumination(n, lamps, queries)
            print('res: %s' % res)
            print('-=' * 20 + '-')


if __name__ == '__main__':
    Solution().test()
