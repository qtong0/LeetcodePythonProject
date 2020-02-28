# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node'):
        if not root: return []
        stack = [root]
        res = []
        while stack:
            node = stack[-1]
            if not node.children:
                res.append(node.val)
                stack.pop()
            while node.children:
                stack.append(node.children.pop())
        return res
