import collections
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        counter = collections.Counter()
        res, j = 0, 0
        for i, num in enumerate(nums):
            if counter[num] == 0:
                k -= 1
            counter[num] += 1
            while k < 0:
                counter[nums[j]] -= 1
                if counter[nums[j]] == 0:
                    k += 1
                j += 1
            res += i - j + 1
        return res


    def test(self):
        testCases = [
            [
                [1,2,1,2,3], 2,
            ],
            [
                [1,2,1,3,4], 3,
            ],
        ]
        for arr, k in testCases:
            res = self.subarraysWithKDistinct(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
