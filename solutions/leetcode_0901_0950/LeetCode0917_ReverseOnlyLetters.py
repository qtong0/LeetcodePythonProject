class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = len(S)-1
        res = ''
        for c in S:
            if c.isalpha():
                tmp = S[i]
                while not tmp.isalpha():
                    i -= 1
                    tmp = S[i]
                i -= 1
                res += tmp
            else:
                res += c
        return res

    def reverseOnlyLetters_own(self, S):
        """
        :type S: str
        :rtype: str
        """
        import re
        l = [None]*len(S)
        for i, c in enumerate(S):
            if not re.match('[a-z]|[A-Z]', c):
                l[i] = c
        j = len(S)-1
        for c in S:
            while j > 0 and l[j] and not re.match('[a-z]|[A-Z]', l[j]):
                j -= 1
            if re.match('[a-z]|[A-Z]', c):
                l[j] = c
                j -= 1
        return ''.join(l)

    def test(self):
        testCases = [
            'ab-cd',
            'a-bC-dEf-ghIj',
            'Test1ng-Leet=code-Q!',
        ]
        for s in testCases:
            res = self.reverseOnlyLetters(s)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
