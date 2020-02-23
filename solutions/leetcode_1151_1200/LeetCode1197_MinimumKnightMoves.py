class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = [([0, 0], 0)]
        visited = set([(0, 0)])
        while queue:
            [i, j], d = queue.pop(0)
            if i == x and j == y:
                return d
            for i0, j0 in (i+1,j+2), (i+2,j+1), (i+2,j-1), (i+1,j-2), \
                        (i-1,j-2), (i-2,j-1), (i-2,j+1), (i-1,j+2):
                if (i0, j0) not in visited:
                    visited.add((i0, j0))
                    queue.append(([i0, j0], d+1))
        return -1

    def test(self):
        testCases = [
            [2, 1],
            [5, 5],
        ]
        for x, y in testCases:
            res = self.minKnightMoves(x, y)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
