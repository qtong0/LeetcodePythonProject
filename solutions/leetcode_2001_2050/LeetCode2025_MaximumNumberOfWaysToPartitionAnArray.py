from typing import List


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        sum_val = sum(nums)
        n = len(nums)
        left_map, right_map = {}, {}
        left = 0
        for i in range(n-1):
            left += nums[i]
            right = sum_val - left
            right_map[left-right] = right_map.get(left-right, 0) + 1
        # without any replacement
        res = right_map.get(0, 0)
        left = 0
        for i in range(n):
            left += nums[i]
            right = sum_val - left
            d = k - nums[i]
            # if we replace nums[i] with k, we will get left_map[d] + right_map[-d] pivots
            res = max(res, left_map.get(d, 0) + right_map.get(-d, 0))
            # transfer the frequency from right_map to left_map
            right_map[left-right] = right_map.get(left-right, 0) - 1
            left_map[left-right] = left_map.get(left-right, 0) + 1
        return res


    # Brute Force
    def waysToPartition_BruteForce(self, nums: List[int], k: int) -> int:
        res = self.getMaxSplits(nums)
        for i, num in enumerate(nums):
            res = max(res, self.getMaxSplits(nums[:i] + [k] + nums[i+1:]))
        return res


    def getMaxSplits(self, nums):
        sum_val = sum(nums)
        pre_sum = 0
        res = 0
        for i in range(len(nums)-1):
            pre_sum += nums[i]
            if pre_sum * 2 == sum_val:
                res += 1
        return res


    def test(self):
        test_cases = [
            [[2,-1,2], 3],
            [[0,0,0], 1],
            [[22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], -33],
        ]
        for nums, k in test_cases:
            res = self.waysToPartition(nums, k)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
