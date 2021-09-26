class Fenwick:
    def __init__(self, n: int):
        self.nums = [0]*(n+1)

    def sum(self, k: int) -> int:
        k += 1
        ans = 0
        while k:
            ans += self.nums[k]
            k &= k-1 # unset last set bit
        return ans

    def add(self, k: int, x: int) -> None:
        k += 1
        while k < len(self.nums):
            self.nums[k] += x
            k += k & -k


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.data = []
        self.value = Fenwick(10**5+1)
        self.index = Fenwick(10**5+1)

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.value.add(num, num)
        self.index.add(num, 1)
        if len(self.data) > self.m:
            num = self.data.pop(0)
            self.value.add(num, -num)
            self.index.add(num, -1)

    def _getindex(self, k):
        lo, hi = 0, 10**5 + 1
        while lo < hi:
            mid = lo + hi >> 1
            if self.index.sum(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m:
            return -1
        lo = self._getindex(self.k)
        hi = self._getindex(self.m-self.k)
        ans = self.value.sum(hi) - self.value.sum(lo)
        ans += (self.index.sum(lo) - self.k) * lo
        ans -= (self.index.sum(hi) - (self.m-self.k)) * hi
        return ans // (self.m - 2*self.k)


# TLE
# My own Binary Search Tree solution, Sadly it's still TLE

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MKAverage_own_BST_Solution:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.deque = []
        self.root = None

    def addElement(self, num: int) -> None:
        node = self.addTreeNode(num, self.root)
        self.deque.append(node)
        if len(self.deque) > self.m:
            node = self.deque.pop(0)
            self.removeTreeNode(self.root, None, node)

    def calculateMKAverage(self) -> int:
        if len(self.deque) < self.m:
            return -1
        sum_val = self.calculateSum(self.root)
        return int(sum_val / (self.m-self.k*2))

    def calculateSum(self, root):
        res = 0
        stack = []
        while root:
            stack.append(root)
            root = root.left
        idx = 0
        while stack:
            node = stack.pop()
            idx += 1
            if self.k+1 <= idx <= self.m-self.k-1:
                res += node.val
                if idx == self.m-self.k-1:
                    break
            while node:
                stack.append(node)
                node = node.left
        return res

    def removeTreeNode(self, root, parent, node):
        if root == node:
            if not parent:
                if root.right:
                    self.root = root.right
                    self.reconstructTreeNode(root.left, root.right)
                else:
                    self.root = root.left
            else:
                if parent.left == root:
                    if root.right:
                        parent.left = root.right
                        self.reconstructTreeNode(root.left, root.right)
                    else:
                        parent.left = root.left
                else:
                    if root.right:
                        parent.right = root.right
                        self.reconstructTreeNode(root.left, root.right)
                    else:
                        parent.right = root.left
        elif node.val < root.val:
            self.removeTreeNode(root.left, root, node)
        else:
            self.removeTreeNode(root.right, root, node)


    def reconstructTreeNode(self, left, root):
        while root and root.left is not None:
            root = root.left
        root.left = left

    def addTreeNode(self, num, root):
        if not self.root:
            self.root = TreeNode(num)
            return self.root
        else:
            if num >= root.val:
                if not root.right:
                    root.right = TreeNode(num)
                    return root.right
                else:
                    return self.addTreeNode(num, root.right)
            else:
                if not root.left:
                    root.left = TreeNode(num)
                    return root.left
                else:
                    return self.addTreeNode(num, root.left)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


if __name__ == '__main__':
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    print(obj.calculateMKAverage())  # -1
    obj.addElement(10)
    print(obj.calculateMKAverage())  # 3
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())  # 5
