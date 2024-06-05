import bisect
from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        cands = []
        for j in range(len(s) - len(b) + 1):
            if s[j: j+len(b)] == b:
                cands.append(j)
        res = []
        for i in range(len(s) - len(a) + 1):
            if s[i: i+len(a)] == a and self.has_matches(i, cands, k):
                res.append(i)
        return res

    def has_matches(self, idx: int, cands: List[int], k: int) -> bool:
        b1 = bisect.bisect_left(cands, idx-k)
        b2 = bisect.bisect_right(cands, idx+k)
        return b1 != b2

    def test(self):
        test_cases = [
            ["isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15],
        ]
        for s, a, b, k in test_cases:
            res = self.beautifulIndices(s, a, b, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
