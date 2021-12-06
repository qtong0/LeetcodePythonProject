# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        if self.dfs(root) == 0:
            self.res += 1
        return self.res

    # 0 - leaf
    # 1 - parent of a leaf
    # 2 - covered, but without camera on this node
    def dfs(self, root):
        if not root:
            return 2
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == 0 or right == 0:
            self.res += 1
            return 1
        return 2 if left == 1 or right == 1 else 0
