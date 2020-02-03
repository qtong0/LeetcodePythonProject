# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode):
        if not root: return []
        hashmap = {}
        self.minKey = float('inf')
        self.maxKey = float('-inf')
        self.helper(root, 0, 0, hashmap)
        res = []
        if not hashmap: return res
        for k in range(int(self.minKey), int(self.maxKey)+1):
            if k in hashmap:
                arr = sorted(hashmap[k], key=lambda x: (-x[0], x[1]))
                res.append([val for _, val in arr])
        return res

    def helper(self, root, x, y, hashmap):
        if root:
            self.minKey = min(self.minKey, x)
            self.maxKey = max(self.maxKey, x)
            hashmap[x] = hashmap.get(x, []) + [(y, root.val)]
            if root.left:
                self.helper(root.left, x-1, y-1, hashmap)
            if root.right:
                self.helper(root.right, x+1, y-1, hashmap)

    def test(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        res = self.verticalTraversal(root)
        print('res: %s' % res)
        print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
