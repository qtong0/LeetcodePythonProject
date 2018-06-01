'''
Created on Mar 14, 2017

@author: MT
'''

class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        left = -1
        maxLen = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        maxLen = max(maxLen, i-left)
                    else:
                        maxLen = max(maxLen, i-stack[-1])
                else:
                    left = i
        return maxLen
    
    def test(self):
        testCases = [
            '(()',
            ')()())',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.longestValidParentheses(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
