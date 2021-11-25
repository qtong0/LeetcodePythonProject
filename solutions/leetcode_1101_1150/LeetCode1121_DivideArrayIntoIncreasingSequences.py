from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        curr = 1
        groups = 1
        n = len(nums)
        for i in range(1, n):
            curr = 1 if nums[i-1] < nums[i] else curr + 1
            groups = max(groups, curr)
        return n >= k * groups


    def test(self):
        test_cases = [
            [[1,2,2,3,3,4,4], 3],
            [[5,6,6,7,8], 3],
        ]
        for nums, k in test_cases:
            res = self.canDivideIntoSubsequences(nums, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
