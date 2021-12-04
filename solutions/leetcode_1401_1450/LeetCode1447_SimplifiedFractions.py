from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            for j in range(1, i):
                g = self.gcm(j, i)
                if g == 1 or (i % g != 0 and i % g != 0):
                    res.append('%s/%s' % (j, i))
        return res

    def gcm(self, a, b):
        while a % b > 0:
            tmp = a % b
            a = b
            b = tmp
        return b


    def test(self):
        test_cases = [
            2,
            3,
            4,
            1,
        ]
        for n in test_cases:
            res = self.simplifiedFractions(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
