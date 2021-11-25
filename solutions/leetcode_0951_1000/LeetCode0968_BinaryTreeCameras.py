# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def solve(node):
            # 0: strict; all nodes below this are covered, but not this one
            # 1: normal; all nodes below and including this are covered - no camera
            # 2: placed camera: all nodes below this are covered, plus camera here
            if not node: return 0, 0, float('inf')
            l = solve(node.left)
            r = solve(node.right)

            dp0 = l[1] + r[1]
            dp1 = min(l[2] + min(r[1:]), r[2] + min(l[1:]))
            dp2 = 1 + min(l) + min(r)

            return dp0, dp1, dp2

        return min(solve(root)[1:])
