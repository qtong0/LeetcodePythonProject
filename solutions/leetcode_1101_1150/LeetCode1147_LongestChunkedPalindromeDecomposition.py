class Solution:
    def longestDecomposition(self, text: str) -> int:
        if not text:
            return 0
        if len(text) == 1:
            return 1
        n = len(text)
        i, j = 0, n-1
        while i < j and text[:i+1] != text[j:]:
            i += 1
            j -= 1
        if i >= j:
            return 1
        else:
            return 2 + self.longestDecomposition(text[i+1:j])

    def test(self):
        test_cases = [
            'ghiabcdefhelloadamhelloabcdefghi',
            'merchant',
            'tpe',
            'antaprezatepzapreanta',
            'aaa',
        ]
        for text in test_cases:
            res = self.longestDecomposition(text)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
