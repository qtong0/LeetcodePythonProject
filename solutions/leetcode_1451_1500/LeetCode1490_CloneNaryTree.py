# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        hashmap = {}
        new_root = Node(root.val, None)
        hashmap[root] = new_root
        queue = [root]
        while queue:
            node = queue.pop(0)
            new_node = hashmap[node]
            for child in node.children:
                queue.append(child)
                if child not in hashmap:
                    new_child = Node(child.val, None)
                    hashmap[child] = new_child
                new_node.children.append(hashmap[child])
        return new_root
