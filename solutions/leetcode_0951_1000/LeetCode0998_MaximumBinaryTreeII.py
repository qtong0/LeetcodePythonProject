# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        l = self.getList(root)
        l.append(val)
        return self.construct(l)

    def getList(self, root):
        node = root
        stack = []
        res = []
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                node0 = node.right
                while node0:
                    stack.append(node0)
                    node0 = node0.left
        return res

    def construct(self, l):
        if not l: return None
        maxVal = max(l)
        idx = l.index(maxVal)
        root = TreeNode(maxVal)
        root.left = self.construct(l[:idx])
        root.right = self.construct(l[idx+1:])
        return root
