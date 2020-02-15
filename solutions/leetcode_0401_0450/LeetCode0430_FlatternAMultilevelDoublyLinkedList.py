# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        prevNode = Node(-1, None, head, None)
        stack = [head]
        while stack:
            node = stack.pop()
            prevNode.next = node
            prevNode.child = None
            node.prev = prevNode
            prevNode = node
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        head.prev = None
        return head

    def test(self):
        node = Node(1, None, Node(2, None, None, None), Node(3, None, None, None))
        res = self.flatten(node)
        print('debug')


if __name__ == '__main__':
    Solution().test()
