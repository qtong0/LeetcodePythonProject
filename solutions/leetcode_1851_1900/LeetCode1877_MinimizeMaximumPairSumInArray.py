from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxPair = float('-inf')
        for i in range(len(nums)//2):
            maxPair = max(maxPair, nums[i]+nums[len(nums)-i-1])
        return maxPair

    def test(self):
        test_cases = [
            [3,5,2,3],
            [3,5,4,2,4,6],
        ]
        for nums in test_cases:
            res = self.minPairSum(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
