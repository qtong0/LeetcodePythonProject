class Solution:
    def minimumDistance(self, word: str) -> int:
        dp, prev_dp = {(0, 0): 0}, {}
        for c in (ord(c)+1 for c in word):
            for a, b in dp:
                prev_dp[c, b] = min(prev_dp.get((c, b), 3000), dp[a, b] + self.d(a, c))
                prev_dp[a, c] = min(prev_dp.get((a, c), 3000), dp[a, b] + self.d(b, c))
            dp, prev_dp = prev_dp, {}
        return min(dp.values())

    def d(self, a, b):
        return a and abs(a//6 - b//6) + abs(a%6 - b%6)



    # DFS, TLE
    def minimumDistance_own_DFS(self, word: str) -> int:
        keyboard = [
            'ABCDEF',
            'GHIJKL',
            'MNOPQR',
            'STUVWX',
            'YZ',
        ]
        self.keymap = {}
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                self.keymap[keyboard[i][j]] = (i, j)
        return self.dfs2('', '', word, 0, 0)

    def dfs2(self, left, right, word, i, curr):
        if i == len(word):
            return curr
        res = float('inf')
        if not left:
            res = min(res, self.dfs2(left+word[i], right, word, i+1, curr))
        else:
            res = min(res, self.dfs2(left+word[i], right, word, i+1, curr + self.dist(left[-1], word[i])))
        if not right:
            res = min(res, self.dfs2(left, right+word[i], word, i+1, curr))
        else:
            res = min(res, self.dfs2(left, right+word[i], word, i+1, curr + self.dist(right[-1], word[i])))
        return res

    def dist(self, c1, c2):
        i1, j1 = self.keymap[c1]
        i2, j2 = self.keymap[c2]
        return abs(i1 - i2) + abs(j1 - j2)



    def test(self):
        test_caes = [
            'CAKE',
            'HAPPY',
            'NEW',
            'YEAR',
            "OPVUWZLCKTDPSUKGHAXIDWHLZFKNBDZEWHBSURTVCADUGTSDMCLDBTAGFWDPGXZBVARNTDICHCUJLNFBQOBTDWMGILXPSFWVGYBZVFFKQIDTOVFAPVNSQJULMVIERWAOXCKXBRI",
        ]
        for word in test_caes:
            res = self.minimumDistance(word)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
