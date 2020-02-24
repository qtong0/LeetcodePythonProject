# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        node = root
        head = node
        stack = []
        while node:
            head = node
            stack.append(node)
            node = node.left
        prevNode = None
        while stack:
            node = stack.pop()
            if prevNode:
                prevNode.right = node
                node.left = prevNode
            prevNode = node
            node0 = node.right
            while node0:
                stack.append(node0)
                node0 = node0.left
        node.right = head
        head.left = node
        return head
