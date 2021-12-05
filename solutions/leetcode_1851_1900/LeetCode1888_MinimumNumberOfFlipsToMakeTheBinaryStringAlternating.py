class Solution:
    # double s
    # sliding n window:
    # |11100|11100 ==> 1|11001|1100 ==> 11|10011|100 and so on
    # when we move one step of the sliding window
    # it is the same to append 1 more element from beginning.
    #
    # TC: O(N)
    # SC: O(N) -> can be optimized to O(1)
    #
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        s0, s1 = '', ''
        for i in range(n*2):
            s0 += '0' if i % 2 == 0 else '1'
            s1 += '1' if i % 2 == 0 else '0'
        res0, res1 = 0, 0
        res = float('inf')
        for i in range(n*2):
            if s[i] != s0[i]:
                res0 += 1
            if s[i] != s1[i]:
                res1 += 1
            # the most left element is outside of sliding window
            # we need to subtract the res if we did `flip` before
            if i >= n:
                if s[i - n] != s0[i - n]:
                    res0 -= 1
                if s[i - n] != s1[i - n]:
                    res1 -= 1
            if i >= n - 1:
                res = min([res, res0, res1])
        return res



    def minFlips_BruteForce_TLE(self, s: str) -> int:
        res = float('inf')
        n = len(s)
        for i in range(n):
            new_s = s[i:] + s[:i]
            res = min(res, self.getRes(new_s, '0', '1'))
            res = min(res, self.getRes(new_s, '1', '0'))
            if res == 0:
                return res
        return res

    def getRes(self, s, c1, c2):
        res = 0
        for i, c in enumerate(s):
            if i % 2 == 0 and c != c1:
                res += 1
            elif i % 2 == 1 and c != c2:
                res += 1
        return res


    def test(self):
        test_cases = [
            '010',
            '111000',
            '1110',
            '100',
            "01001001101",
        ]
        for s in test_cases:
            res1 = self.minFlips(s)
            res2 = self.minFlips_BruteForce_TLE(s)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
