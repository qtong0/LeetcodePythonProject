class Solution:
    # If ch[i] > ch[j], we can swap these characters
    #
    # Collect indexes of all characters 0-9 of the source strings in idx.
    # For each characters, we track which indexes we have used in pos.
    #
    # For each character ch in the target string, check if we have it in idx.
    # If so, verify that there are no smaller characters in front of it.
    # To do that, we check the current idexes of all characters less than ch.
    #
    # If the character can be moved, mark its index as used by advancing pos[ch].
    #
    def isTransformable(self, s: str, t: str) -> bool:
        idx = [[] for _ in range(10)]
        pos = [0]*10
        for i, c in enumerate(s):
            idx[int(c)].append(i)
        for c in t:
            d = int(c)
            if pos[d] >= len(idx[d]):
                return False
            for i in range(d):
                if pos[i] < len(idx[i]) and idx[i][pos[i]] < idx[d][pos[d]]:
                    return False
            pos[d] += 1
        return True


    def test(self):
        test_cases = [
            ["84532", "34852"],
            ["34521", "23415"],
            ["12345", "12435"],
            ["1", "2"],
        ]
        for s, t in test_cases:
            res = self.isTransformable(s, t)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
