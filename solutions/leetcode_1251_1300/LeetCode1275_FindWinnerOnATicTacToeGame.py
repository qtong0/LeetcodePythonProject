from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0]*3
        cols = [0]*3
        dia = 0
        anti = 0
        for i, (x, y) in enumerate(moves):
            toAdd = -1 if i%2 else 1
            rows[x] += toAdd
            cols[y] += toAdd
            if x == y:
                dia += toAdd
            if x + y == 2:
                anti += toAdd
            if 3 in rows or 3 in cols or 3 in (dia, anti):
                return 'A'
            if -3 in rows or -3 in cols or -3 in (dia, anti):
                return 'B'
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'


    def test(self):
        test_cases = [
            [[0,0],[2,0],[1,1],[2,1],[2,2]],
            [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]],
            [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]],
            [[0,0],[1,1]],
        ]
        for moves in test_cases:
            res = self.tictactoe(moves)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
