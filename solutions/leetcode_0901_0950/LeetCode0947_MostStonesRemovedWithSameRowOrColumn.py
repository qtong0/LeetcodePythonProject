from typing import List


class Solution(object):
    def removeStones(self, stones: List[List[int]]) -> int:
        union_find = {}
        for i, j in stones:
            root1 = self.find(union_find, i)
            root2 = self.find(union_find, ~j)
            union_find[root2] = root1
        return len(stones) - len({self.find(union_find, x) for x in union_find})

    def find(self, union_find, x):
        while x != union_find.setdefault(x, x):
            x = union_find[x]
        return x


    def test(self):
        test_cases = [
            [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],
            [[0,0],[0,2],[1,1],[2,0],[2,2]],
            [[0,0]],
        ]
        for stones in test_cases:
            res = self.removeStones(stones)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
