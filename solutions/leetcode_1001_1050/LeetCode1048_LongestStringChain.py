class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        n = len(words)
        dp = [1]*n
        hashmap = {}
        res = 0
        for i in range(n-1, -1, -1):
            w = words[i]
            hashmap[len(w)] = hashmap.get(len(w), []) + [i]
            for j in hashmap.get(len(w)+1, []):
                if self.isPredecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res

    def isPredecessor(self, s1, s2):
        i, j = 0, 0
        diff = False
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if diff: return False
                diff = True
                j += 1
            else:
                i += 1
                j += 1
        return True


    def test(self):
        testCases = [
            # ["a","b","ba","bca","bda","bdca"],
            ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"],
            ["wnyxmflkf","xefx","usqhb","ttmdvv","hagmmn","tmvv","pttmdvv","nmzlhlpr","ymfk","uhpaglmmnn","zckgh","hgmmn","isqxrk","isqrk","nmzlhpr","uysyqhxb","haglmmn","xfx","mm","wymfkf","tmdvv","uhaglmmn","mf","uhaglmmnn","mfk","wnymfkf","powttkmdvv","kwnyxmflkf","xx","rnqbhxsj","uysqhb","pttkmdvv","hmmn","iq","m","ymfkf","zckgdh","zckh","hmm","xuefx","mv","iqrk","tmv","iqk","wnyxmfkf","uysyqhb","v","m","pwttkmdvv","rnqbhsj"],
        ]
        for words in testCases:
            res = self.longestStrChain(words)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
