# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        queue = [self.root]
        prevQueue = []
        currQueue = []
        nextQueue = []
        num = -1
        while queue:
            node = queue.pop(0)
            currQueue.append(node)
            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)
            if not queue:
                if nextQueue:
                    prevQueue = currQueue
                    currQueue = []
                queue = nextQueue
                nextQueue = []
                num += 1
        if 2**num == len(currQueue):
            self.parents = currQueue
        else:
            self.parents = prevQueue

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = None
        nextParents = []
        for node in self.parents:
            if not node.left:
                parent = node
                node.left = TreeNode(v)
                nextParents.append(node.left)
                break
            else:
                nextParents.append(node.left)
            if not node.right:
                parent = node
                node.right = TreeNode(v)
                nextParents.append(node.right)
                break
            else:
                nextParents.append(node.right)
        if parent == self.parents[-1] and parent.right:
            self.parents = nextParents
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

if __name__ == '__main__':
    root = TreeNode(1)
    cbt = CBTInserter(root)
    print(cbt.insert(2))
    print(cbt.insert(3))
    print(cbt.get_root())

    # root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    # cbt = CBTInserter(root)
    # print(cbt.insert(7))
    # print(cbt.insert(8))
    # print(cbt.get_root())
