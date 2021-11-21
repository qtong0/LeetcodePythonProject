from typing import List


class DSU:
    def __init__(self, n):
        self.roots = list(range(n))


    def find(self, idx):
        while self.roots[idx] != idx:
            idx = self.roots[idx]
        return idx


    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        self.roots[root1] = root2


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu, res = DSU(n), []
        for x, y in requests:
            rootx, rooty = dsu.find(x), dsu.find(y)
            restricted = True
            for a, b in restrictions:
                roota, rootb = dsu.find(a), dsu.find(b)
                if set([roota, rootb]) == set([rootx, rooty]):
                    restricted = False
                    break
            res.append(restricted)
            if restricted:
                dsu.union(x, y)
        return res


    def test(self):
        test_cases = [
            [3, [[0,1]], [[0,2],[2,1]]],
            [3, [[0,1]], [[1,2],[0,2]]],
            [5, [[0,1],[1,2],[2,3]], [[0,4],[1,2],[3,1],[3,4]]],
        ]
        for n, restrictions, requests in test_cases:
            res = self.friendRequests(n, restrictions, requests)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
