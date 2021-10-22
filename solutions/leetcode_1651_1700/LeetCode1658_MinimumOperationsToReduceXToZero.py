from typing import List


class Solution:
    # O(N)
    def minOperations(self, nums: List[int], x: int) -> int:
        curr_sum = sum(nums)
        left = 0
        res = float('inf')
        n = len(nums)

        for right in range(n):
            curr_sum -= nums[right]
            while curr_sum < x and left <= right:
                curr_sum += nums[left]
                left += 1
            if curr_sum == x:
                res = min(res, (n-1-right)+left)

        return res if res != float('inf') else -1

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
