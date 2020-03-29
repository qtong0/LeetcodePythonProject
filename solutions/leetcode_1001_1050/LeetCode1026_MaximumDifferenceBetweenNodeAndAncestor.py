# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # only tracking max and min values - faster, use this!
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0
        min_max = [float('inf'), float('-inf')]
        self.res = float('-inf')
        self.dfs(root, min_max)
        return self.res

    def dfs(self, root, min_max):
        if root:
            minVal, maxVal = min_max[0], min_max[1]
            if minVal != float('inf') and maxVal != float('-inf'):
                self.res = max(self.res, abs(root.val-minVal), abs(maxVal-root.val))
            min_max = [min(minVal, root.val), max(maxVal, root.val)]
            self.dfs(root.left, min_max)
            self.dfs(root.right, min_max)



    # My own first time solution is Slow O(N*N)
    def maxAncestorDiff_own(self, root: TreeNode) -> int:
        if not root: return -1
        self.res = float('-inf')
        ancestors = set()
        self.helper(root, ancestors)
        return self.res

    def helper(self, root, ancestors):
        if root:
            for val0 in ancestors:
                self.res = max(self.res, abs(val0-root.val))
            ancestors.add(root.val)
            self.helper(root.left, ancestors)
            self.helper(root.right, ancestors)
            ancestors.discard(root.val)
