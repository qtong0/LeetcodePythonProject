class Solution:
    def modifyString(self, s: str) -> str:
        res = ''
        n = len(s)
        for i, c in enumerate(s):
            if c != '?':
                res += c
            else:
                if i == 0 and i == n-1:
                    res += 'a'
                elif i == 0:
                    for j in range(26):
                        cand = chr(ord('a') + j)
                        if cand != s[i+1]:
                            res += cand
                            break
                elif i == n-1:
                    for j in range(26):
                        cand = chr(ord('a') + j)
                        if cand != res[-1]:
                            res += cand
                            break
                else:
                    prevc = res[-1]
                    nextc = s[i+1]
                    for j in range(26):
                        cand = chr(ord('a') + j)
                        if cand != prevc and cand != nextc:
                            res += cand
                            break
        return res

    def test(self):
        test_cases = []
        for s in test_cases:
            res = self.modifyString(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
