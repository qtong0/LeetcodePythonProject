class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        hashmap = {}
        for i in range(5):
            for j in range(5):
                c = board[i][j]
                hashmap[c] = [i, j]
        hashmap['z'] = [5, 0]
        res = ''
        prev = 'a'
        for c in target:
            if c != prev:
                x, y = hashmap[prev]
                i, j = hashmap[c]
                if i > x:
                    if j > y:
                        res += 'R' * (j-y)
                    else:
                        res += 'L' * (y-j)
                    res += 'D' * (i-x)
                else:
                    res += 'U' * (x-i)
                    if j > y:
                        res += 'R' * (j-y)
                    else:
                        res += 'L' * (y-j)
            res += '!'
            prev = c
        return res

    def test(self):
        test_cases = [
            'leet',
            'code',
        ]
        for target in test_cases:
            res = self.alphabetBoardPath(target)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
