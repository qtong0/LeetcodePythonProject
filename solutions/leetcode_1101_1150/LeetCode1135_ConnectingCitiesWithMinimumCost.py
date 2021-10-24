from typing import List


class Solution:
    # Union Find !!!
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        roots = {city: city for city in range(1, n+1)}
        connections.sort(key=lambda x: x[2])
        res = 0
        for c1, c2, cost in connections:
            if self.union(roots, c1, c2):
                res += cost
        root = self.find(roots, 1)
        if all(root == self.find(roots, city) for city in range(1, n+1)):
            return res
        else:
            return -1

    def find(self, roots, node):
        while node != roots[node]:
            node = roots[node]
        return node

    def union(self, roots, c1, c2):
        root1, root2 = self.find(roots, c1), self.find(roots, c2)
        if root1 == root2:
            return False
        roots[root2] = root1
        return True


    def test(self):
        test_cases = [
            [4, [[1,2,1],[1,3,2],[3,4,4],[1,4,3]]],
            [3, [[1,2,5],[1,3,6],[2,3,1]]],
            [4, [[1,2,3],[3,4,4]]],
        ]
        for n, connections in test_cases:
            res = self.minimumCost(n, connections)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
