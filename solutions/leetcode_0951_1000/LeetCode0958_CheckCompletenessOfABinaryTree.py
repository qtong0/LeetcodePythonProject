# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        nextQueue = []
        found = False
        num = 1
        while queue:
            node = queue.pop(0)
            if node.left:
                if found: return False
                nextQueue.append(node.left)
            else:
                found = True
            if node.right:
                if found: return False
                nextQueue.append(node.right)
            else:
                found = True
            if not queue:
                num *= 2
                if len(nextQueue) != num:
                    if not found:
                        return False
                queue = nextQueue
                nextQueue = []
        return True

    def test(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        res = self.isCompleteTree(root)
        print('res: %s' % res)
        print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
