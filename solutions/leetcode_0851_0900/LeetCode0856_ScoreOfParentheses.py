class Solution(object):
    # SC O(1)
    def scoreOfParentheses(self, s: str) -> int:
        bal = 0
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    res += 1 << bal
        return res


    # SC O(N)
    def scoreOfParentheses_SPACE(self, s: str) -> int:
        stack, cur = [], 0
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur


    def test(self):
        testCases = [
            '()',
            '(())',
            '()()',
            '(())()',
            '(()(()))',
        ]
        for s in testCases:
            res = self.scoreOfParentheses(s)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
