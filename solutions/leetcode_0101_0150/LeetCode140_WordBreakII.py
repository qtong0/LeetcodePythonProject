from typing import List


class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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

    def wordBreak_DFS_MEMO(self, s: str, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res


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
