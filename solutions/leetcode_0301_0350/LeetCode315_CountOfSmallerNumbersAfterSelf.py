from typing import List


class TreeNode(object):
    def __init__(self, val):
        self.dup = 1
        self.num = 0
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    # merge sort solution
    def countSmaller(self, nums):
        def sort(indexes):
            half = len(indexes) // 2
            if half:
                left, right = sort(indexes[:half]), sort(indexes[half:])
                for i in range(len(indexes))[::-1]:
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        smaller[left[-1]] += len(right)
                        indexes[i] = left.pop()
                    else:
                        indexes[i] = right.pop()
            return indexes
        smaller = [0] * len(nums)
        sort(list(range(len(nums))))
        return smaller


    # Tree solution, TLE
    def countSmaller_tree_TLE(self, nums: List[int]) -> List[int]:
        root = None
        res = []
        for i in range(len(nums)-1, -1, -1):
            root, val = self.buildTree(root, nums[i], 0)
            res.insert(0, val)
        return res

    def buildTree(self, root, num, val):
        if not root:
            root = TreeNode(num)
        else:
            if root.val == num:
                val += root.num
                root.dup += 1
            elif root.val > num:
                root.num += 1
                root.left, val = self.buildTree(root.left, num, val)
            else:
                val += root.num + root.dup
                root.right, val = self.buildTree(root.right, num, val)
        return root, val
    
    def test(self):
        testCases = [
            [5, 2, 6, 1],
            [-1, -1],
            [3, 2, 2, 6, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            res_1 = self.countSmaller(nums)
            res_2 = self.countSmaller_tree_TLE(nums)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*20+'-')


if __name__ == '__main__':
    Solution().test()
