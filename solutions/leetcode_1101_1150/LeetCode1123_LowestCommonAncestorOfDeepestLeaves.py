# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root: return None
        return self.helper(root)

    # returning dept, node
    def helper(self, root):
        if not root: return 0, None
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left[0] == right[0]:
            return left[0]+1, root
        elif left[0] > right[0]:
            return left[0]+1, left[1]
        else:
            return right[0]+1, right[1]
