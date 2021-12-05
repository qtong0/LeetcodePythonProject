from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        currList = []
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                currList.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(currList)
            currList = []
        return res
