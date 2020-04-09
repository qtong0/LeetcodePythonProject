# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # O(N) solution
    def bstFromPreorder(self, preorder) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        stack = [root]
        n = len(preorder)
        for i in range(1, n):
            # take the last element of the stack as a parent
            # and create a child from the next preorder element
            node, child = stack[-1], TreeNode(preorder[i])
            # adjust the parent
            while stack and stack[-1].val < child.val:
                node = stack.pop()
            # follow BST logic to create a parent-child link
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
                # add the child into stack
            stack.append(child)
        return root

    # My own O(N*Log(N)) solution, passing LC, should be fine too???
    def bstFromPreorder_own(self, preorder) -> TreeNode:
        if not preorder: return None
        val = preorder[0]
        root = TreeNode(val)
        i = 1
        while i < len(preorder) and preorder[i] < val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
