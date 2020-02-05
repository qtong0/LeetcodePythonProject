# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root, None)]
        xParent = None
        yParent = None
        nextQueue = []
        while queue:
            node, parent = queue.pop(0)
            if node.val == x:
                xParent = parent
                if yParent:
                    if yParent == xParent:
                        return False
                    else:
                        return True
            elif node.val == y:
                yParent = parent
                if xParent:
                    if xParent == yParent:
                        return False
                    else:
                        return True
            if node.left:
                nextQueue.append((node.left, node))
            if node.right:
                nextQueue.append((node.right, node))
            if not queue:
                if xParent or yParent: return False
                queue = nextQueue
                nextQueue = []
                xParent, yParent = None, None
        return False

    def test(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        print(self.isCousins(root, 4, 3))


if __name__ == '__main__':
    Solution().test()
