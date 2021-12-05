class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        if abs(ones - zeros) > 1:
            return -1
        if ones == zeros:
            res0 = self.getRes(s, '0', '1')
            res1 = self.getRes(s, '1', '0')
            return min(res0, res1)
        elif ones > zeros:
            return self.getRes(s, '1', '0')
        else:
            return self.getRes(s, '0', '1')

    def getRes(self, s, c1, c2):
        res = 0
        for i, c in enumerate(s):
            if i % 2 == 0 and c != c1:
                res += 1
            elif i % 2 == 1 and c != c2:
                res += 1
        return res // 2


    def test(self):
        test_cases = [
            '010',
            '111000',
            '1110',
            '100',
        ]
        for s in test_cases:
            res = self.minSwaps(s)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
