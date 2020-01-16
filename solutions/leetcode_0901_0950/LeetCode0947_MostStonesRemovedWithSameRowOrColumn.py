class DSU:
    def __init__(self, n):
        self.roots = range(n)

    def find(self, x):
        while x != self.roots[x]:
            x = self.roots[x]
        return self.roots[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.roots[xr] = yr


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y+10000)
        return n - len({dsu.find(x) for x, y in stones})
