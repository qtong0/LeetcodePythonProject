from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        counter = {}
        for c in words[0]:
            counter[c] = counter.get(c, 0) + 1
        for i in range(1, len(words)):
            w = words[i]
            new_counter = {}
            for c in w:
                if c in counter:
                    new_counter[c] = new_counter.get(c, 0) + 1
            for c in new_counter:
                new_counter[c] = min(counter[c], new_counter[c])
            counter = new_counter
        res = []
        for c, freq in counter.items():
            res += [c]*freq
        return res


    def test(self):
        test_cases = [
            ["bella","label","roller"],
            ["cool","lock","cook"],
        ]
        for words in test_cases:
            res = self.commonChars(words)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
