# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        if not s: return None
        i = 0
        while i < len(s) and s[i] != '(':
            i += 1
        val = s[:i]
        root = TreeNode(val)
        i += 1
        if i < len(s):
            prev = i
            count = 1
            while i < len(s) and count > 0:
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                i += 1
            node = self.str2tree(s[prev:i-1])
            root.left = node
        i += 1
        if i < len(s):
            node = self.str2tree(s[i:-1])
            root.right = node
        return root
