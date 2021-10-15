from typing import List
import math


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        maxPow = int(math.log(n, 2)) + 1
        dp = [[0]*n for _ in range(maxPow)]
        dp[0] = parent
        for i in range(1, maxPow):
            for j in range(n):
                pre = dp[i-1][j]
                if pre == -1:
                    dp[i][j] = pre
                else:
                    dp[i][j] = dp[i-1][pre]
        self.dp = dp
        self.maxPow = maxPow

    # O(Log(N))
    def getKthAncestor(self, node: int, k: int) -> int:
        row = self.maxPow
        while k > 0 and node > -1:
            # same as
            # k >= 1 << maxPow
            if k >= 2 ** row:
                node = self.dp[row][node]
                # same as
                # k -= 1 << maxPow
                k -= 2 ** row
            else:
                row -= 1
        return node



# O(k) is too slow
class TreeAncestor_too_slow:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        hashmap = {}
        for i, p in enumerate(parent):
            hashmap[i] = p
        self.parents_map = hashmap

    def getKthAncestor(self, node: int, k: int) -> int:
        for _ in range(k):
            if node not in self.parents_map or self.parents_map[node] == -1:
                return -1
            node = self.parents_map[node]
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
