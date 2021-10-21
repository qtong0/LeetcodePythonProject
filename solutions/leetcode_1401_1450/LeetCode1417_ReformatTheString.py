class Solution:
    def reformat(self, s: str) -> str:
        sc, sd = '', ''
        for c in s:
            if c.isdigit():
                sd += c
            else:
                sc += c
            if len(sd) > len(s) // 2 + 1 or len(sc) > len(s) // 2 + 1:
                return ''
        if abs(len(sc) - len(sd)) > 1:
            return ''
        res = ''
        s1, s2 = (sc, sd) if len(sc) > len(sd) else (sd, sc)
        for i in range(len(s)):
            if i % 2 == 0:
                res += s1[i//2]
            else:
                res += s2[(i-1)//2]
        return res

    def test(self):
        test_cases = [
            'a0b1c2',
            'leetcode',
            '1229857369',
            'covid2019',
            'ab123',
        ]
        for s in test_cases:
            res = self.reformat(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
