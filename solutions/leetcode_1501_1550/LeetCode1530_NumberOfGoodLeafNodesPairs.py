# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        self.helper(root, distance)
        return self.count

    def helper(self, node, distance):
        if not node:
            return []
        if not node.left and not node.right:
            return [[node, 0]]
        left = self.helper(node.left, distance)
        right = self.helper(node.right, distance)
        res = [[node, h+1] for node, h in left + right]
        for l, hl in left:
            for r, hr in right:
                if hl+1 + hr+1 <= distance:
                    self.count += 1
        return res


    def test(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        res = self.countPairs(root, 3)
        print('res: %s' % res)
        print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
