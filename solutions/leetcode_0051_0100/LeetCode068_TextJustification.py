class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append( cur[0] + ' '*(maxWidth - num_of_letters) )
                else:
                    num_spaces = maxWidth - num_of_letters
                    space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1 )
                    for i in range(num_extra_spaces):
                        cur[i] += ' '
                    res.append((' '*space_between_words).join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        res.append(' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1))
        return res


    def fullJustify_another(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth-num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]


    def test(self):
        testCases = [
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
        ]
        for words, maxWidth in testCases:
            print('words: %s' % (words))
            print('maxWidth: %s' % (maxWidth))
            result = self.fullJustify(words, maxWidth)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()