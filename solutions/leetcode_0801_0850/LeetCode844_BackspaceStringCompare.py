class Solution(object):
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S)-1, len(T)-1
        skipS, skipT = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True


    def backspaceCompare_SPACE(self, S: str, T: str) -> bool:
        def build(s):
            res = []
            for c in s:
                if c != '#':
                    res.append(c)
                else:
                    res.pop()
            return res
        return build(S) == build(T)
    
    def test(self):
        testCases = [
            ["ab#c", "ad#c"],
            ["ab##", "c#d#"],
            ["a##c", "#a#c"],
            ["a#c", "b"],
        ]
        for s, t in testCases:
            result = self.backspaceCompare(s, t)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
