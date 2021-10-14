# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    # two runners
    # O(N + M) - N, M are heights of two nodes
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        n1, n2 = p, q
        while n1 != n2:
            n1 = q if n1 is None else n1.parent
            n2 = p if n2 is None else n2.parent
        return n1

    # This works, but not the best, two passes
    def lowestCommonAncestor_own(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        while root.parent:
            root = root.parent
        return self.helper(root, p, q)

    def helper(self, root, node1, node2):
        if not root:
            return None
        if root == node1:
            return node1
        if root == node2:
            return node2
        left = self.helper(root.left, node1, node2)
        right = self.helper(root.right, node1, node2)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None


if __name__ == '__main__':
    root, left, right = Node(3), Node(5), Node(1)
    root.left = left
    left.parent = root
    root.right = right
    right.parent = root

    res = Solution().lowestCommonAncestor(left, right)
    print('res: %s' % res.val)
