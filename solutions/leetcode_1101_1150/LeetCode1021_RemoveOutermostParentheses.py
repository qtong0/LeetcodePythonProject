class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        curr = ''
        for c in S:
            if c == '(':
                stack.append(c)
                curr += c
            else:
                if len(stack) == 1:
                    stack.pop()
                    res += curr[1:]
                    curr = ''
                else:
                    curr += c
                    stack.pop()
        return res
