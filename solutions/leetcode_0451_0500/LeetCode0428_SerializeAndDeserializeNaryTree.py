# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        l = []
        self.serializeHelper(root, l)
        return ','.join(l)

    def serializeHelper(self, root, l):
        if not root:
            return None
        else:
            l.append(str(root.val))
            l.append(str(len(root.children)))
            for child in root.children:
                self.serializeHelper(child, l)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        queue = data.split(',')
        return self.deserializeHelper(queue)

    def deserializeHelper(self, queue):
        root = Node()
        root.val = int(queue.pop(0))
        size = int(queue.pop(0))
        root.children = []
        for _ in range(size):
            root.children.append(self.deserializeHelper(queue))
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == '__main__':
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    codec = Codec()
    print(codec.serialize(root))
    print('-='*30+'-')
    root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
                    Node(4, [Node(8, [Node(12)])]),
                    Node(5, [Node(9, [Node(13)]), Node(10)])])
    print(codec.serialize(root))
    print('-='*30+'-')
