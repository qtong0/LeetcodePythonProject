class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        i, j = 0, 0
        res = ''
        while A > 0 or B > 0:
            writeA = False
            l = len(res)
            if l >= 2 and res[-1] == res[-2]:
                if res[-1] == 'b':
                    writeA = True
            else:
                if A >= B:
                    writeA = True
            if writeA:
                A -= 1
                res += 'a'
            else:
                B -= 1
                res += 'b'
        return res

    def test(self):
        testCases = [
            [1, 3],
            [1, 2],
            [4, 1],
        ]
        for a, b in testCases:
            res = self.strWithout3a3b(a, b)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
