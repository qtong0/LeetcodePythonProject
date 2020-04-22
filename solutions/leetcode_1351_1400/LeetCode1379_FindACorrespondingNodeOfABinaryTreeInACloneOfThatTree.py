# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node, node0 = original, cloned
        if not node: return None
        stack = [(node, node0)]
        while stack:
            node, node0 = stack.pop()
            if node == target:
                return node0
            if node.right:
                stack.append((node.right, node0.right))
            if node.left:
                stack.append((node.left, node0.left))
        return None
