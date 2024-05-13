class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if c + d == e + f:
            if c + d == a + b and (c < a < e or e < a < c):
                return 2
            return 1
        if c - d == e - f:
            if c - d == a - b and (c < a < e or e < a < c):
                return 2
            return 1
        if a == e:
            if a == c and (b < d < f or f < d < b):
                return 2
            return 1
        if b == f:
            if b == d and (a < c < e or e < c < a):
                return 2
            return 1
        return 2

    def test(self):
        test_cases = [
            [1, 1, 8, 8, 2, 3],
            [5, 3, 3, 4, 5, 2],
            [4, 3, 3, 4, 5, 2],
            [1, 6, 3, 3, 5, 6],
        ]
        for a, b, c, d, e, f in test_cases:
            res = self.minMovesToCaptureTheQueen(a, b, c, d, e, f)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
