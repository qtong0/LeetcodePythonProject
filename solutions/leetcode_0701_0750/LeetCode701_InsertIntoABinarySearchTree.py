# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # My Own solution
    def insertIntoBST_bfs(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        found = False
        while stack:
            node = stack.pop()
            if node.val > val:
                found = True
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    nodeAdd = node.left
                    while nodeAdd.right:
                        nodeAdd = nodeAdd.right
                    nodeAdd.right = TreeNode(val)
                break
            node0 = node.right
            while node0:
                stack.append(node0)
                node0 = node0.left
        if not found:
            while node.right:
                node = node.right
            node.right = TreeNode(val)
        return root
