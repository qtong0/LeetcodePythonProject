'''
Created on May 5, 2017

@author: MT
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(n):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] != '.' and p[j-1] != s[i]:
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
        return dp[-1][-1]
