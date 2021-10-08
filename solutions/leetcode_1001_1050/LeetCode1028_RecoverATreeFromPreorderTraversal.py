from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Best solution is using stack, but I think my solution can pass too
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, i = [], 0
        s = traversal
        while i < len(s):
            level, val = 0, ''
            while i < len(s) and s[i] == '-':
                level, i = level+1, i+1
            while i < len(s) and s[i] != '-':
                val, i = val + s[i], i+1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

    # Own solution, slower
    def recoverFromPreorder_own(self, traversal: str) -> Optional[TreeNode]:
        return self.helper(traversal, 1)

    def helper(self, s, level):
        arr = self.splitByLevel(s, level)
        if not arr:
            return None
        root = TreeNode(int(arr[0]))
        if len(arr) >= 2:
            left = self.helper(arr[1], level+1)
            root.left = left
        if len(arr) == 3:
            right = self.helper(arr[2], level+1)
            root.right = right
        return root

    def splitByLevel(self, s, level):
        res = []
        prev = 0
        n = len(s)
        i = 0
        while i < n:
            j = i
            while i < n and s[i] == '-':
                i += 1
            if level == i-j:
                res.append(s[prev:j])
                prev = i
            while i < n and s[i] != '-':
                i += 1
        res.append(s[prev:])
        return res

    def test(self):
        test_cases = [
            # '1-2--3--4-5--6--7',
            '1-2--3---4-5--6---7',
            # '1-401--349---90--88',
        ]
        for s in test_cases:
            res = self.recoverFromPreorder(s)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
