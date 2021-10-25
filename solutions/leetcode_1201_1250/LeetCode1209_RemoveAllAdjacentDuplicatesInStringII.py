class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            j = i+1
            while j < len(s) and s[j] == c:
                j += 1
            t = j-i
            if t % k != 0:
                if stack and stack[-1][0] == c:
                    stack[-1][1] += t
                    while stack[-1][1] >= k:
                        stack[-1][1] -= k
                    if stack[-1][1] == 0:
                        stack.pop()
                else:
                    stack.append([c, t])
            i = j
        res = ''
        for c, t in stack:
            res += c*t
        return res

    def test(self):
        test_cases = [
            ["deeedbbcccbdaa", 3],
            ["abcd", 2],
            ["pbbcggttciiippooaais", 2],
            ["iiiixxxxxiiccccczzffffflllllllllfffffllyyyyyuuuuuz", 5],
        ]
        for s, k in test_cases:
            res = self.removeDuplicates(s, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
