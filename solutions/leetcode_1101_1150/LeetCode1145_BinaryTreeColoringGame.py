# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.left_count = 0
        self.right_count = 0

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.count(root, x)

        # if player 2 chooses player 1's parent node and player 1 node's count is smaller than n/2
        # player 2 will win
        if self.left_count + self.right_count + 1 < n/2:
            return True

        # if player 2 chooses player 1's left or right node and it's count is bigger than n/2
        # player 2 will win
        if self.left_count > n/2 or self.right_count > n/2:
            return True

        return False

    def count(self, node, x):
        if not node:
            return 0
        l, r = self.count(node.left, x), self.count(node.right, x)
        if node.val == x:
            self.left_count, self.right_count = l, r
        return l + r + 1
