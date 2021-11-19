from typing import List


class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        stack = []
        max_val = float('-inf')
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num > max_val:
                stack.append(num)
            max_val = max(max_val, num)
        return len(stack)


    def test(self):
        test_cases = [
            [7],
            [-1,5,2],
            [1,2,3,4,5],
        ]
        for nums in test_cases:
            res = self.binarySearchableNumbers(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
