# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root: return ''
        self.minVal = None
        self.helper(root, chr(ord('a')+root.val))
        return self.minVal

    def helper(self, root, curr):
        if not root.left and not root.right and curr:
            if not self.minVal:
                self.minVal = curr[::-1]
            else:
                self.minVal = min(self.minVal, curr[::-1])
        if root.left:
            self.helper(root.left, curr+chr(ord('a')+root.left.val))
        if root.right:
            self.helper(root.right, curr+chr(ord('a')+root.right.val))
