class Solution:
    def numSplits(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0
        hashset = set()
        left_nums = [0] * len(s)
        for i, c in enumerate(s):
            hashset.add(c)
            left_nums[i] = len(hashset)
        res = 0
        hashset.clear()
        for i in range(len(s)-2, -1, -1):
            hashset.add(s[i+1])
            if len(hashset) == left_nums[i]:
                res += 1
        return res

    def test(self):
        testCases = [
            'aacaba',
            'abcd',
            'aaaaa',
            'acbadbaada',
        ]
        for s in testCases:
            res = self.numSplits(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
