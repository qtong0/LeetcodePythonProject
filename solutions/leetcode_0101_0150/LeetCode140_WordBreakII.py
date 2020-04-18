class Solution(object):
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        if not s: return []
        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[0].append('')
        for i in range(1, n+1):
            curList = []
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    for l in dp[j]:
                        if l:
                            curList.append(l + ' ' + s[j:i])
                        else:
                            curList.append(s[j:i])
                dp[i] = curList
        return dp[-1]


    # My own solution, difficult to figure out the time complexity
    def wordBreak_own(self, s: str, wordDict):
        if not s: return []
        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for w in wordDict:
                if dp[i] and i+len(w) < n+1 and s[i:i+len(w)] == w:
                    dp[i+len(w)].append(w)
        res = []
        self.helper(n, res, [], dp)
        return res

    def helper(self, i, res, curr, dp):
        if i <= 0:
            if i == 0:
                res.append(' '.join(curr))
            return
        for w in dp[i]:
            curr.insert(0, w)
            self.helper(i-len(w), res, curr, dp)
            curr.pop(0)
    
    def test(self):
        testCases = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ]
        for s, wordDict in testCases:
            print('s: %s' % (s))
            print('wordDict: %s' % (wordDict))
            result = self.wordBreak(s, wordDict)
            print('result: %s' % (result))
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
