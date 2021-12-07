from typing import List
import heapq


class Solution:
    # Binary Search + Sliding Window
    def kthSmallestSubarraySum_slow(self, nums: List[int], k: int) -> int:
        l, r = 1, 20000*50000
        n = len(nums)
        while l < r:
            mid = (l + r) // 2
            floor = 0
            sum_val = 0
            i, j = 0, 0
            while i < n:
                if sum_val + nums[i] <= mid:
                    sum_val += nums[i]
                    i += 1
                    floor += i - j
                else:
                    sum_val -= nums[j]
                    j += 1
            if floor < k:
                l = mid + 1
            else:
                r = mid
        return l



    def kthSmallestSubarraySum_slow(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0]
        heap = []
        for num in nums:
            preSum.append(preSum[-1] + num)
        for i in range(n):
            for j in range(i+1):
                sum_val = preSum[i+1] - preSum[j]
                heapq.heappush(heap, -sum_val)
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heapq.heappop(heap)



    def test(self):
        test_cases = [
            [[2,1,3], 4],
            [[3,3,5,5], 7],
        ]
        for nums, k in test_cases:
            res = self.kthSmallestSubarraySum(nums, k)
            print('res: %s' % res)
            print('-='*30 + '-')



if __name__ == '__main__':
    Solution().test()
