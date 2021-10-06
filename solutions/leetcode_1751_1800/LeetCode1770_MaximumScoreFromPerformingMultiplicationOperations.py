from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        dp = [0] * (len(multipliers) + 1)
        for idx, mul in enumerate(multipliers):
            len_remain = n - idx - 1
            dp[n-len_remain] = dp[n-len_remain-1] + mul*nums[n-len_remain-1]
            for j in range(n-len_remain-1, 0, -1):
                dp[j] = max(
                    dp[j] + mul * nums[j+len_remain],
                    dp[j-1] + mul * nums[j-1]
                )
            dp[0] += mul * nums[len_remain]
        return max(dp)

    # DFS + Mem is TLE :(
    def maximumScore_own_TLE(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        mem = [[float('-inf')]*n for _ in range(n)]
        return self.dfs(mem, nums, 0, n-1, multipliers, 0)

    def dfs(self, mem, nums, i, j, mult, curr):
        if not mult:
            return curr
        if mem[i][j] != float('-inf'):
            return mem[i][j]
        res = max(self.dfs(mem, nums, i+1, j, mult[1:], curr+mult[0]*nums[i]),
                  self.dfs(mem, nums, i, j-1, mult[1:], curr+mult[0]*nums[j]))
        return res

    def test(self):
        test_cases = [
            [[1,2,3], [3,2,1]],
            [[-5,-3,-3,-2,7,1], [-10,-5,3,4,6]],
        ]
        for nums, multipliers in test_cases:
            res_1 = self.maximumScore(nums, multipliers)
            res_2 = self.maximumScore_own_TLE(nums, multipliers)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
