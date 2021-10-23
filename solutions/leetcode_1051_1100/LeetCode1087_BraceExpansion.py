from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, '', res)
        return res

    def dfs(self, s, i, curr, res):
        if i == len(s):
            res.append(curr)
            return
        if s[i] != '{':
            self.dfs(s, i+1, curr+s[i], res)
        else:
            j = i+1
            while j < len(s) and s[j] != '}':
                j += 1
            substr = s[i+1:j]
            arr = substr.split(',')
            arr.sort()
            for sub in arr:
                self.dfs(s, j+1, curr+sub, res)

    def test(self):
        test_cases = [
            '{a,b}c{d,e}f',
            'abcd',
        ]
        for s in test_cases:
            res = self.expand(s)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
