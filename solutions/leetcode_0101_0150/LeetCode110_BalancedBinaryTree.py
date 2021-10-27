# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return True, -1
        leftIsBalance, leftHeight = self.helper(root.left)
        if not leftIsBalance:
            return False, 0
        rightIsBalance, rightHeight = self.helper(root.right)
        if not rightIsBalance:
            return False, 0
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)




    def isBalanced_slow(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        else:
            return abs(self.getHeight(root.left)-self.getHeight(root.right)) <= 1 and\
                self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, root):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return max(leftHeight, rightHeight) + 1
