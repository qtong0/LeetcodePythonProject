class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            s, res = self.remove(s, 'ab', x)
            res += self.remove(s, 'ba', y)[1]
        else:
            s, res = self.remove(s, 'ba', y)
            res += self.remove(s, 'ab', x)[1]
        return res

    # return new_s, res
    def remove(self, s, pattern, point):
        stack, res = [], 0
        for i in range(len(s)):
            stack.append(s[i])
            while len(stack) >= 2 and stack[-2] + stack[-1] == pattern:
                res += point
                stack.pop()
                stack.pop()
        new_s = ''.join(stack)
        return new_s, res


    def maximumGain_own_TLE(self, s: str, x: int, y: int) -> int:
        return self.dfs(s, x, y, {})

    def dfs(self, s, x, y, memo):
        if s in memo:
            return memo[s]
        res = 0
        for i in range(len(s)-1):
            sub = s[i:i+2]
            if sub == 'ab':
                res = max(res, x + self.dfs(s[:i] + s[i+2:], x, y, memo))
            elif sub == 'ba':
                res = max(res, y + self.dfs(s[:i] + s[i+2:], x, y, memo))
        memo[s] = res
        return res


    def test(self):
        test_cases = [
            ["cdbcbbaaabab", 4, 5],
            ["aabbaaxybbaabb", 5, 4],
        ]
        for s, x, y in test_cases:
            res1 = self.maximumGain(s, x, y)
            res2 = self.maximumGain_own_TLE(s, x, y)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
