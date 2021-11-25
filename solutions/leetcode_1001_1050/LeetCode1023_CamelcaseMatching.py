from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            res.append(self.match(query, pattern))
        return res

    def match(self, query, pattern):
        j = 0
        n = len(pattern)
        for i, c in enumerate(query):
            if self.isUpper(c):
                if j >= n or pattern[j] != c:
                    return False
                else:
                    j += 1
            elif j < n and c == pattern[j]:
                j += 1
        return j == n

    def isUpper(self, c):
        return ord('A') <= ord(c) <= ord('Z')


    def test(self):
        test_cases = [
            [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"],
            [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"],
            [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"],
        ]
        for queries, pattern in test_cases:
            res = self.camelMatch(queries, pattern)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
