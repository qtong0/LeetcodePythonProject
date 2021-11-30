from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = nums[0]
        deque = []
        for i in range(n):
            if deque:
                nums[i] += deque[0]
            res = max(res, nums[i])
            while deque and nums[i] > deque[-1]:
                deque.pop()
            if nums[i] > 0:
                deque.append(nums[i])
            if i >= k and deque and deque[0] == nums[i-k]:
                deque.pop(0)
        return res


    def test(self):
        test_cases = [
            [[10,2,-10,5,20], 2],
            [[-1,-2,-3], 1],
            [[10,-2,-10,-5,20], 2],
        ]
        for nums, k in test_cases:
            res = self.constrainedSubsetSum(nums, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
