# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.diameter = 0
        self.helper(root)
        return self.diameter-1

    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.diameter = max(self.diameter, l+r+1)
        return 1+max(l, r)
    
    def test(self):
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        for root in testCases:
            result = self.diameterOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
