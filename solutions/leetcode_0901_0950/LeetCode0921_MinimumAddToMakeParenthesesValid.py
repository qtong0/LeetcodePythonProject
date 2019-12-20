class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0
        for i, c in enumerate(S):
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    res += 1
                else:
                    stack.pop()
        res += len(stack)
        return res

    def test(self):
        testCases = [
            '())',
            '(((',
            '()',
            '()))((',
        ]
        for s in testCases:
            res = self.minAddToMakeValid(s)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
