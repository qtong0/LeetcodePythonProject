# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        if not root: return []
        hashset = set(to_delete)
        res, queue = set([root]), []
        queue = [(root, None)]
        while queue:
            node, parent = queue.pop(0)
            if node.val in hashset:
                res.discard(node)
                if node.left:
                    res.add(node.left)
                if node.right:
                    res.add(node.right)
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        return list(res)
