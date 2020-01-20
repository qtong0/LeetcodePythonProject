class DSU(object):
    def __init__(self, n):
        self.roots = list(range(n))

    def find(self, val):
        while val != self.roots[val]:
            val = self.roots[val]
        return val

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.roots[xr] = yr


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        dsu = DSU(4*n*n)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4*(r*n + c)
                if val in '/ ':
                    dsu.union(root+0, root+1)
                    dsu.union(root+2, root+3)
                if val in '\\ ':
                    dsu.union(root+0, root+2)
                    dsu.union(root+1, root+3)

                # north/south
                if r+1 < n: dsu.union(root+3, (root+4*n)+0)
                if r-1 >= 0: dsu.union(root+0, (root-4*n)+3)

                # east/west
                if c+1 < n: dsu.union(root+2, (root+4)+1)
                if c-1 >= 0: dsu.union(root+1, (root-4)+2)

        return sum(dsu.find(x) == x for x in range(4*n*n))
