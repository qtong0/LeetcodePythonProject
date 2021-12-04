# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        if p in q.children:
            return root

        dummy = Node()
        dummy.children.append(root)

        p_parent = self.dfs_parent(dummy, p)
        q_in_p = self.dfs_parent(p, q)

        p_index = p_parent.children.index(p)
        p_parent.children.pop(p_index)

        q.children.append(p)
        if q_in_p:
            q_in_p.children.remove(q)
            p_parent.children.insert(p_index, q)

        return dummy.children[0]


    def dfs_parent(self, node, target):
        if target in node.children:
            return node
        for child in node.children:
            res = self.dfs_parent(child, target)
            if res:
                return res
        return None
