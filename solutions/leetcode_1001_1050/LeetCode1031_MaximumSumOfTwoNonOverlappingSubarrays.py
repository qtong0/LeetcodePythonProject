from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # Convert to PreSum
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        res, firstLenMax, secondLenMax = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]

        # window | --- firstLen --- | --- secondLen --- |
        for i in range(firstLen + secondLen, len(nums)):
            firstLenMax = max(firstLenMax, nums[i - secondLen] - nums[i - firstLen - secondLen])
            res = max(res, firstLenMax + nums[i] - nums[i - secondLen])

        # window | --- secondLen --- | --- firstLen --- |
        for i in range(firstLen + secondLen, len(nums)):
            secondLenMax = max(secondLenMax, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, secondLenMax + nums[i] - nums[i - firstLen])

        return res

    def test(self):
        test_cases = [
            [[0,6,5,2,2,5,1,9,4], 1, 2],
            [[3,8,1,3,2,1,8,9,0], 3, 2],
            [[2,1,5,6,0,9,5,0,3,8], 4, 3],
        ]
        for nums, firstLen, secondLen in test_cases:
            res = self.maxSumTwoNoOverlap(nums, firstLen, secondLen)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
