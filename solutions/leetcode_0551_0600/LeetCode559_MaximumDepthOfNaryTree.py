# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        maxLen = 1
        queue = [(root, 1)]
        while queue:
            node, length = queue.pop(0)
            maxLen = max(maxLen, length)
            for child in node.children:
                queue.append((child, length+1))
        return maxLen
