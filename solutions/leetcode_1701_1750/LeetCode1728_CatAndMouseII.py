from functools import lru_cache
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        mouse_pos = cat_pos = None
        available = 0 # available steps for mouse and cat
        # search for start pos of mouse and cat
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    available += 1
                if grid[i][j] == 'M':
                    mouse_pos = (i, j)
                elif grid[i][j] == 'C':
                    cat_pos = (i, j)

        @lru_cache(None)
        def dp(turn, mouse_pos, cat_pos):
            # if turn == m*n*2
            # we already searched the whole grid
            if turn == available * 2:
                return False
            if turn % 2 == 0:
                # mouse turn
                i, j = mouse_pos
                for di, dj in dirs:
                    for jump in range(mouseJump + 1):
                        new_i, new_j = i + di*jump, j + dj*jump
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '#':
                            if dp(turn + 1, (new_i, new_j), cat_pos) or grid[new_i][new_j] == 'F':
                                return True
                        else:
                            break
                return False
            else:
                # cat turn
                i, j = cat_pos
                for di, dj in dirs:
                    for jump in range(catJump + 1):
                        new_i, new_j = i + di*jump, j + dj*jump
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '#':
                            if not dp(turn+1, mouse_pos, (new_i, new_j)) or (new_i, new_j) == mouse_pos or grid[new_i][new_j] == 'F':
                                return False
                        else:
                            break
                return True
        return dp(0, mouse_pos, cat_pos)


    def test(self):
        test_cases = [
            [["M.C...F"], 1, 4],
            [["M.C...F"], 1, 3],
            [["C...#","...#F","....#","M...."], 2, 5],
            [[".M...","..#..","#..#.","C#.#.","...#F"], 3, 1],
        ]
        for grid, catJump, mouseJump in test_cases:
            res = self.canMouseWin(grid, catJump, mouseJump)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
