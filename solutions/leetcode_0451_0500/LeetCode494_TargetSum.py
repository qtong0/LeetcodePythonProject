from typing import List


class Solution(object):
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        idx = len(nums)-1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, target, idx, curr_sum)

    def dp(self, nums, target, idx, curr_sum):
        if (idx, curr_sum) in self.memo:
            return self.memo[(idx, curr_sum)]

        if idx < 0 and curr_sum == target:
            return 1
        if idx < 0:
            return 0

        positive = self.dp(nums, target, idx-1, curr_sum + nums[idx])
        negative = self.dp(nums, target, idx-1, curr_sum - nums[idx])

        self.memo[(idx, curr_sum)] = positive + negative
        return self.memo[(idx, curr_sum)]



    # doesn't work any more, target can be negative
    def findTargetSumWays_orig(self, nums: List[int], target: int) -> int:
        sumVal = sum(nums)
        if sumVal < target or (sumVal+target) % 2 != 0:
            return 0
        target = (sumVal+target)//2
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for i in range(target, -1, -1):
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]



    def test(self):
        testCases = [
            [
                [100],
                -200,
            ],
            [
                [1, 1, 1, 1, 1],
                3,
            ],
            [
                [1,2,7,9,981],
                1000000000,
            ],
        ]
        for nums, S in testCases:
            print('nums: %s' % nums)
            print('S: %s' % S)
            result = self.findTargetSumWays(nums, S)
            print('result: %s' % result)
            print('-='*30+'-')



if __name__ == '__main__':
    Solution().test()
