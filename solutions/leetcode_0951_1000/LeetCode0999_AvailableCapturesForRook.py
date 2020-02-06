class Solution:
    def numRookCaptures(self, board) -> int:
        m, n = len(board), len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                        if self.captures(board, i, j, x, y):
                            res += 1
        return res

    def captures(self, board, i, j, x, y):
        m, n = len(board), len(board[0])
        while 0 <= i+x < m and 0 <= j+y < n:
            i += x
            j += y
            if board[i][j] == 'B':
                return False
            elif board[i][j] == 'p':
                return True
        return False
