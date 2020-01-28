# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage):
        res, idx = [], [0]
        return res if self.helper(root, voyage, res, idx) else [-1]

    def helper(self, root, voyage, res, idx):
        if not root: return True
        if root.val != voyage[idx[0]]:
            return False
        idx[0] += 1
        if self.helper(root.left, voyage, res, idx) and \
                self.helper(root.right, voyage, res, idx):
            return True
        if self.helper(root.right, voyage, res, idx) and \
                self.helper(root.left, voyage, res, idx):
            res.append(root.val)
            return True
        return False

    def test(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        voyage = [1, 2, 3]
        res = self.flipMatchVoyage(root, voyage)
        print('res: %s' % res)


if __name__ == '__main__':
    Solution().test()
