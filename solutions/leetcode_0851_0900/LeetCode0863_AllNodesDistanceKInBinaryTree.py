# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        hashmap = {}
        self.find(root, target, hashmap)
        res = []
        self.dfs(root, K, hashmap[root], res, hashmap)
        return res
    
    def find(self, root, target, hashmap):
        if not root: return -1
        if root == target:
            hashmap[root] = 0
            return 0
        left = self.find(root.left, target, hashmap)
        if left >= 0:
            hashmap[root] = left+1
            return left+1
        right = self.find(root.right, target, hashmap)
        if right >= 0:
            hashmap[root] = right+1
            return right+1
        return -1
    
    def dfs(self, root, k, length, res, hashmap):
        if not root: return
        if root in hashmap:
            length = hashmap[root]
        if length == k:
            res.append(root.val)
        self.dfs(root.left, k, length+1, res, hashmap)
        self.dfs(root.right, k, length+1, res, hashmap)


if __name__ == '__main__':
    root = TreeNode(3, None, TreeNode(1, TreeNode(0), TreeNode(8)))
    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root.left = target

    res = Solution().distanceK(root, target, 2)
    print('res: %s' % res)
