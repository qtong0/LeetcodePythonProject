class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        res = set()
        xi, yi = 0, 0
        while x**xi + y**yi <= bound:
            res.add(x**xi + y**yi)
            if y != 1 and x**xi + y**(yi+1) <= bound:
                yi += 1
            elif x != 1:
                xi += 1
                yi = 0
            else:
                break
        return list(res)

    def test(self):
        testCases = [
            # [2, 3, 10],
            # [3, 5, 15],
            [2, 1, 10],
            [1, 2, 10],
        ]
        for x, y, bound in testCases:
            res = self.powerfulIntegers(x, y, bound)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
