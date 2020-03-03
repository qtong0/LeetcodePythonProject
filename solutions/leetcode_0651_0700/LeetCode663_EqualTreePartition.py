'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None,right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return 0
        hashmap = {}
        sumVal = self.dfs(root, hashmap)
        if sumVal != 0:
            return sumVal/2.0 in hashmap
        else:
            return hashmap.get(sumVal/2.0, 0) > 1

    def dfs(self, node, hashmap):
        res = node.val
        if node.left:
            res += self.dfs(node.left, hashmap)
        if node.right:
            res += self.dfs(node.right, hashmap)
        hashmap[res] = hashmap.get(res, 0)+1
        return res

    def test(self):
        testCases = [
            TreeNode(0, TreeNode(-1), TreeNode(1)),
            TreeNode(5, TreeNode(10), TreeNode(10, TreeNode(2), TreeNode(3))),
            TreeNode(1, TreeNode(2), TreeNode(10, TreeNode(2), TreeNode(20))),
            TreeNode(1, TreeNode(-1)),
            TreeNode(1, None, TreeNode(2)),
            TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(2, TreeNode(3))), TreeNode(3)),
        ]
        for root in testCases:
            result = self.checkEqualTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
