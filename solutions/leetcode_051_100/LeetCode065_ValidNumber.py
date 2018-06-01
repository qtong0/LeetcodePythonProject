'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        i, e = 0, length-1
        while i <= e and s[i] == ' ': i+=1
        if i > length-1: return False
        while e >= i and s[e] == ' ': e-=1
        if s[i] == '+' or s[i] == '-': i+=1
        num, dot, exp = False, False, False
        while i <= e:
            c = s[i]
            if c.isdigit(): num = True
            elif c == '.':
                if exp or dot:
                    return False
                dot = True
            elif c == 'e':
                if exp or num is False:
                    return False
                exp = True
                num = False
            elif c == '+' or c == '-':
                if s[i-1] != 'e': return False
            else:
                return False
            i+=1
        return num
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()