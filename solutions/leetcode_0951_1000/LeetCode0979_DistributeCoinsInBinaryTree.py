# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = [0]
        self.helper(root, res)
        return res[0]

    def helper(self, root, res):
        if not root: return 0
        left = self.helper(root.left, res)
        right = self.helper(root.right, res)
        plus = left+right+root.val-1
        res[0] += abs(plus)
        return plus
