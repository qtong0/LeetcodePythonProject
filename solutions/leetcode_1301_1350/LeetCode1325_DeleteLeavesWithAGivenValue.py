from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        else:
            return root

    # own solution
    def removeLeafNodes_own(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        while True:
            is_removed, root = self.removeHelper(root, target)
            if not is_removed:
                break
        return root

    # is_removed, node
    def removeHelper(self, node, target):
        if not node:
            return False, node
        if not node.left and not node.right and node.val == target:
            return True, None
        left_removed, left = self.removeHelper(node.left)
        right_removed, right = self.removeHelper(node.right)
        node.left = left
        node.right = right
        return left_removed or right_removed, node
