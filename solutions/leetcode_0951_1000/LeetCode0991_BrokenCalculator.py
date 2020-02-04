class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            res += 1
            if Y%2 != 0:
                Y += 1
            else:
                Y //= 2
        return res + (X-Y)

    def test(self):
        testCases = [
            [2,3],
            [5,8],
            [3,10],
            [1024,1],
            [1,1000000000],
        ]
        for x, y in testCases:
            res = self.brokenCalc(x, y)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
