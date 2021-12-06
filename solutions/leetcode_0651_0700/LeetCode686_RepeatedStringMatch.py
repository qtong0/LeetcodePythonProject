class Solution(object):
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n1, n2 = len(a), len(b)
        k = n2//n1+2
        if str(a*k).count(b) == 0:
            return -1
        while k >= 1 and str(a*k).count(b) != 0:
            k -= 1
        return k+1


    def test(self):
        testCases = [
            [
                'abcd',
                'cdabcdab',
            ]
        ]
        for A, B in testCases:
            print('A: %s' % A)
            print('B: %s' % B)
            result = self.repeatedStringMatch(A, B)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
