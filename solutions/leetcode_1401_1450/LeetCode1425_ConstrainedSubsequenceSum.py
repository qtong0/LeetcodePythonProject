from typing import List


class Solution:
    # Similar to LC 239 Sliding Window Maximum
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = nums[0]
        # `deque` stores dp[i - k], dp[i-k+1], .., dp[i - 1] whose values are larger than 0 in a decreasing order
        # Note that the length of `deque` is not necessarily `k`.
        # The values smaller than dp[i-1] will be discarded. If u r confused, go on and come back later.
        deque = []
        for i in range(n):
            # deque[0] is the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1])
            if deque:
                nums[i] += deque[0]
            res = max(res, nums[i])
            # 1. We always want to retrieve the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1]) from `deque`
            # 2. We expect dp[i] to be added to `deque` so that we can compute dp[i + 1] in the next iteration
            # 3. So, if dp[i] is larger than some old values, we can discard them safely.
            # 4. As a result, the length of `deque` is not necessarily `k`
            while deque and nums[i] > deque[-1]:
                deque.pop()
            # no need to store the negative value
            if nums[i] > 0:
                deque.append(nums[i])
            # we do not need the value of A[i - k] when computing dp[i+1] in the next iteration,
            # because `j - i <= k` has to be satisfied.
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
