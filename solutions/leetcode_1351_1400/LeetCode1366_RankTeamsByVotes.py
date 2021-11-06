from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        counter = {}
        indexes = {}
        n = len(votes[0])
        for v in votes:
            for i, c in enumerate(v):
                counter[c] = counter.get(c, 0) + 1
                if c not in indexes:
                    indexes[c] = [0]*n
                indexes[c][i] -= 1
        arr = sorted([[-counter[c], indexes[c], c] for c in counter.keys()])
        return ''.join([a[2] for a in arr])


    def test(self):
        test_cases = [
            ["ABC","ACB","ABC","ACB","ACB"],
            ["WXYZ","XYZW"],
            ["ZMNAGUEDSJYLBOPHRQICWFXTVK"],
            ["BCA","CAB","CBA","ABC","ACB","BAC"],
            ["M","M","M","M"],
        ]
        for votes in test_cases:
            res = self.rankTeams(votes)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
