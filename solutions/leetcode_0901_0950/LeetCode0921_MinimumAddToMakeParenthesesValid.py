class Solution(object):
    def minAddToMakeValid(self, S: str) -> int:
        res, bal = 0, 0
        for c in S:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            # it is guaranteed bal >= -1
            if bal == -1:
                res += 1
                bal += 1
        return res + bal



    # My own solution
    def minAddToMakeValid_SPACE(self, S: str) -> int:
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
