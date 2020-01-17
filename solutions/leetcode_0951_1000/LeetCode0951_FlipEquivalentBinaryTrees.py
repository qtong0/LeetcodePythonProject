# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return root1.val == root2.val and \
                (self.flipEquiv(root1.left, root2.left) and
                    self.flipEquiv(root1.right, root2.right)) or \
                (self.flipEquiv(root1.right, root2.left) and
                    self.flipEquiv(root1.left, root2.right))

    def test(self):
        root1 = TreeNode(0, TreeNode(3, TreeNode(1)), TreeNode(2))
        root2 = TreeNode(0, TreeNode(3, TreeNode(1, TreeNode(2))))
        res = self.flipEquiv(root1, root2)
        print('res: %s' % res)


if __name__ == '__main__':
    Solution().test()
