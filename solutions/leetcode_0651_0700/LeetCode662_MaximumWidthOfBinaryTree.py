'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [(root, 0, 0)]
        cur_dept = 0
        left = 0
        res = 0
        while queue:
            node, depth, pos = queue.pop(0)
            if node.left:
                queue.append((node.left, depth+1, pos*2))
            if node.right:
                queue.append((node.right, depth+1, pos*2+1))
            if cur_dept != depth:
                cur_dept = depth
                left = pos
            res = max(res, pos-left+1)
        return res


    def widthOfBinaryTree_DFS(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root, 0, 0, {})
        return self.res

    def dfs(self, node, depth, pos, leftMap):
        if depth not in leftMap:
            leftMap[depth] = pos
        self.res = max(self.res, pos-leftMap[depth]+1)
        if node.left:
            self.dfs(node.left, depth+1, pos*2, leftMap)
        if node.right:
            self.dfs(node.right, depth+1, pos*2+1, leftMap)


    def test(self):
        testCases = [
            TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))),
            TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3))),
            TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
            TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, None, TreeNode(7)))),
        ]
        for root in testCases:
            result = self.widthOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
