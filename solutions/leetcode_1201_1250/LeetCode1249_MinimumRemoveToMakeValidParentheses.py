class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        adding = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    adding.add(stack.pop())
                    adding.add(i)
        res = ''
        for i, c in enumerate(s):
            if i in adding or c not in '()':
                res += c
        return res

    def test(self):
        testCases = [
            'lee(t(c)o)de)',
            'a)b(c)d',
            '))((',
            '(a(b(c)d)',
        ]
        for s in testCases:
            res = self.minRemoveToMakeValid(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
