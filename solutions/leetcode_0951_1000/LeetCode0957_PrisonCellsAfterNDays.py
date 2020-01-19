class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = self.nextday(cells)
        return cells

    def nextday(self, cells):
        return [int(0 < i < 7 and cells[i - 1] == cells[i + 1]) for i in range(8)]

    def test(self):
        testCases = [
            [[0,1,0,1,1,0,0,1], 7],
            [[1,0,0,1,0,0,1,0], 1000000000],
        ]
        for cells, n in testCases:
            res = self.prisonAfterNDays(cells, n)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
