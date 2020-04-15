# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # O(N) solution
    def bstFromPreorder(self, preorder) -> TreeNode:
        idx = [0]
        return self.helper(preorder, float('inf'), idx)

    def helper(self, preorder, upper, idx):
        if idx[0] == len(preorder) or preorder[idx[0]] > upper:
            return None
        root = TreeNode(preorder[idx[0]])
        idx[0] += 1
        root.left = self.helper(preorder, root.val, idx)
        root.right = self.helper(preorder, upper, idx)
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
