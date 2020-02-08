class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        if len(set(str2)) == 26:
            return False
        hashmap = {}
        n = len(str1)
        for c1, c2 in zip(str1, str2):
            if c1 not in hashmap:
                hashmap[c1] = c2
            else:
                if hashmap[c1] != c2:
                    return False
        return True

    def test(self):
        testCases = [
            ['aabcc', 'ccdee'],
            ["leetcode", "codeleet"],
            [
                "abcdefghijklmnopqrstuvwxyz",
                "bcdefghijklmnopqrstuvwxyza",
            ],
            [
                "abcdefghijklmnopqrstuvwxyz",
                "bcdefghijklmnopqrstuvwxyzq",
            ],
        ]
        for s1, s2 in testCases:
            res = self.canConvert(s1, s2)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
