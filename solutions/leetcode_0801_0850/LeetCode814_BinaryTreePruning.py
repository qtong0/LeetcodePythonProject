# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        left  = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if left is None and right is None and root.val == 0:
            return None
        else:
            root.left = left
            root.right = right
            return root



if __name__ == '__main__':
    Solution().test()
