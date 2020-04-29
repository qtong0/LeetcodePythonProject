# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    # O(N)
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.helper(root)
        return self.count

    def helper(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            self.count += 1
            return True
        isUnival = True
        if root.left:
            isUnival = self.helper(root.left) and isUnival and root.val == root.left.val
        if root.right:
            isUnival = self.helper(root.right) and isUnival and root.val == root.right.val
        if not isUnival:
            return False
        self.count += 1
        return isUnival



    def countUnivalSubtrees_orig(self, root: TreeNode) -> int:
        res = 0
        if not root: return res
        if self.isUniVal(root):
            res += 1
        res += self.countUnivalSubtrees(root.left)+ \
               self.countUnivalSubtrees(root.right)
        return res

    def isUniVal(self, root):
        if not root.left and not root.right:
            return True
        if not root.right:
            return root.val == root.left.val and self.isUniVal(root.left)
        if not root.left:
            return root.val == root.right.val and self.isUniVal(root.right)
        return root.left.val == root.val and root.right.val == root.val and \
               self.isUniVal(root.left) and self.isUniVal(root.right)
