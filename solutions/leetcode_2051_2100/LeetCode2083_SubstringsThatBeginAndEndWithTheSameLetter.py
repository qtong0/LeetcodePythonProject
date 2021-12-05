class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr = [0]*26
        res = 0
        for c in s:
            arr[ord(c) - ord('a')] += 1
            res += arr[ord(c) - ord('a')]
        return res


    def test(self):
        test_caess = [
            'abcba',
            'abacad',
            'a',
        ]
        for s in test_caess:
            res = self.numberOfSubstrings(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
