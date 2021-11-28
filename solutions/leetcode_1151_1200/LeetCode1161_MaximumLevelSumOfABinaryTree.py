from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        res = 0
        level = 1
        queue = [root]
        while queue:
            sum_val = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                sum_val += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum_val > max_val:
                max_val = sum_val
                res = level
            level += 1
        return res
