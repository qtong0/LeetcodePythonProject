class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        hashmap = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        i, j = 0, len(s)-1
        all_same = True
        while i <= j:
            if s[i] in hashmap and s[j] in hashmap:
                if hashmap[s[i]] != s[j] or hashmap[s[j]] != s[i]:
                    all_same = False
            else:
                return False
            i += 1
            j -= 1
        return not all_same

    def test(self):
        test_cases = [
            6,
            89,
            11,
            25,
        ]
        for n in test_cases:
            res = self.confusingNumber(n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
