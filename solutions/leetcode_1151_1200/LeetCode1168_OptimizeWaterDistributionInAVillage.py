class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes):
        roots = list(range(n+1))
        sizes = [1]*(n+1)
        for i, cost in enumerate(wells):
            pipes.append([0, i+1, cost])
        res = 0
        pipes.sort(key=lambda x: x[-1])
        for h1, h2, cost in pipes:
            root1 = self.getRoot(roots, h1)
            root2 = self.getRoot(roots, h2)
            if root1 != root2:
                if sizes[root1] < sizes[root2]:
                    root1, root2 = root2, root1
                roots[root2] = root1
                sizes[root1] += sizes[root2]
                res += cost
                n -= 1
            if n == 0:
                return res
        return res

    def getRoot(self, roots, node):
        while node != roots[node]:
            node = roots[node]
        return node

    # this works too, but much slower
    def minCostToSupplyWater_slower(self, n: int, wells, pipes):
        roots = list(range(n+1))
        for i, cost in enumerate(wells):
            pipes.append([0, i+1, cost])
        res = 0
        pipes.sort(key=lambda x: x[-1])
        for h1, h2, cost in pipes:
            root1 = self.getRoot(roots, h1)
            root2 = self.getRoot(roots, h2)
            if root1 != root2:
                n -= 1
                roots[root2] = root1
                res += cost
            if n == 0:
                return res
        return res
