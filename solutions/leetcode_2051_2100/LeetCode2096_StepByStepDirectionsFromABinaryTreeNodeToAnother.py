from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Own Solution, I think it's still O(N)
    # Just multiple passes
    # Sadly, TLE
    #
    def getDirections_own_TLE(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if startValue == destValue:
            return ''
        common = self.commonAncester(root, startValue, destValue)
        start_steps, _ = self.bfs(common, startValue)
        _, dest_path = self.bfs(common, destValue)
        return 'U'*start_steps + dest_path

    def bfs(self, root, target):
        queue = [[root, '']]
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node, path = queue.pop(0)
                if node.val == target:
                    return steps, path
                if node.left:
                    queue.append([node.left, path + 'L'])
                if node.right:
                    queue.append([node.right, path + 'R'])
            steps += 1
        return steps, ''

    def commonAncester(self, root, val1, val2):
        if not root:
            return None
        if root.val == val1 or root.val == val2:
            return root
        left = self.commonAncester(root.left, val1, val2)
        right = self.commonAncester(root.right, val1, val2)
        if left and right:
            return root
        elif left or right:
            return left if left else right
        else:
            return None
