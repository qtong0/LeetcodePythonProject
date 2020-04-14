class Solution(object):
    # O(n**2)
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s)-1
        while j >= 0:
            if s[i] == s[j]:
                i += 1
            j -= 1
        if i == len(s):
            return s
        mid = s[:i]
        suffix = s[i:]
        return suffix[::-1]+self.shortestPalindrome(mid)+suffix

    # KMP <=> O(n)
    def shortestPalindrome_kmp(self, s):
        tmp = s + '#' + s[::-1]
        tbl = self.getTable(tmp)
        return s[tbl[-1]:][::-1] + s

    def getTable(self, s):
        tbl = [0]*len(s)
        idx = 0
        for i in range(1, len(s)):
            if s[idx] == s[i]:
                tbl[i] = tbl[i-1]+1
                idx += 1
            else:
                idx = tbl[i-1]
                while idx > 0 and s[idx] != s[i]:
                    idx = tbl[idx-1]
                if s[idx] == s[i]:
                    idx += 1
                tbl[i] = idx
        return tbl

    
    def test(self):
        testCases = [
            'aacecaaa',
            'abcd',
            'aacecabccaa',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.shortestPalindrome(s)
            res = self.shortestPalindrome_kmp(s)
            print('result: %s' % result)
            print('res: %s' % res)
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
