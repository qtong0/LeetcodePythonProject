class Solution:
    def reorderSpaces(self, text: str) -> str:
        prev = 0
        words = []
        spaces = 0
        for i, c in enumerate(text):
            if c == ' ':
                spaces += 1
                if 0 <= prev < i:
                    words.append(text[prev:i])
                prev = i+1
        if 0 <= prev < len(text):
            words.append(text[prev:])
        if len(words) == 0:
            return text
        elif len(words) == 1:
            return words[0] + ' '*(len(text) - len(words[0]))
        new_spaces, last = divmod(spaces, len(words)-1)
        return (' '*new_spaces).join(words) + ' '*last

    def test(self):
        test_cases = [
            '  this   is  a sentence ',
            ' practice   makes   perfect',
            'hello   world',
            '  walks  udp package   into  bar a',
            'a',
        ]
        for text in test_cases:
            res = self.reorderSpaces(text)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
