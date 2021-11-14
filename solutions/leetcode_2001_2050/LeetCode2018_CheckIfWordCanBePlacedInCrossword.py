from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m and len(word) > n:
            return False
        for i in range(m):
            for j in range(n):
                if self.matchHorizotal(board, i, j, word) or\
                        self.matchVertical(board, i, j, word) or\
                        self.matchHorizotal(board, i, j, word[::-1]) or\
                        self.matchVertical(board, i, j, word[::-1]):
                    return True
        return False


    def matchHorizotal(self, board, i, j, word):
        n = len(board[0])
        if j == 0 or board[i][j-1] == '#':
            k = 0
            while k < len(word) and j+k < n and board[i][j+k] in (word[k], ' '):
                k += 1
            if k == len(word) and (j + k == n or board[i][j+k] == '#'):
                return True
        return False

    def matchVertical(self, board, i, j, word):
        m = len(board)
        if i == 0 or board[i-1][j] == '#':
            k = 0
            while k < len(word) and i+k < m and board[i+k][j] in (word[k], ' '):
                k += 1
            if k == len(word) and (i + k == m or board[i+k][j] == '#'):
                return True
        return False


    def test(self):
        test_cases = [
            [[["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "abc"],
            [[[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], "ac"],
            [[["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], "ca"],
        ]
        for board, word in test_cases:
            res = self.placeWordInCrossword(board, word)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
