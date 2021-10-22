from typing import List


class Solution:
    # O(N)
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        sum_val = 0
        hashmap = {0: -1}
        res = float('-inf')

        for i, num in enumerate(nums):
            sum_val += num
            if sum_val - target in hashmap:
                res = max(res, i - hashmap[sum_val - target])
            hashmap[sum_val] = i
        return len(nums) - res if res != float('-inf') else -1

    def test(self):
        test_cases = [
            [[1,1,4,2,3], 5],
            [[5,6,7,8,9], 4],
            [[3,2,20,1,1,3], 10],
            [[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365],
        ]
        for nums, x in test_cases:
            res = self.minOperations(nums, x)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
