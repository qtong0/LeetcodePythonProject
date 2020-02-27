# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        node0 = node
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        node = node0
        while node.parent and node == node.parent.right:
            node = node.parent
        if not node.parent or node == node.parent.right:
            return None
        node = node.parent
        return node
