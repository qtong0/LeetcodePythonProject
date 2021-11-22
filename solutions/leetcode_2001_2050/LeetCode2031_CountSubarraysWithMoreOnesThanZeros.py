from typing import List


class Solution:
    ###
    # The trick is that it doesn't matter where the ranges are, only what they sum up to a certain number.
    # Consider a position j that holds a 1. Let's say the total sum [0,j] is 3.
    # Then any range [i,j-1] that is zero can be found by counting ranges [0,i] such that the sum is 3-1 = 2:
    #
    # |------------3-----------|
    # [ 0, ..., i, ..., j-1, j ]
    # |-----2-----|----0---|-1-|
    #
    # So, for each position, the current sum is added to a "prefix sum counter".
    # This counter can be used to calculate how many previously invalid sums now meet the criterion,
    # or how many have become invalid.
    #
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sumCount = {0: 1}
        res = 0
        validCount, sumVal = 0, 0
        for num in nums:
            if num == 0:
                validCount = (validCount - sumCount.get(sumVal-1, 0)) % MOD
                sumVal -= 1
            else:
                validCount = (validCount + sumCount.get(sumVal, 0)) % MOD
                sumVal += 1
            sumCount[sumVal] = sumCount.get(sumVal, 0) + 1
            res = (res + validCount) % MOD
        return res


    def subarraysWithMoreZerosThanOnes_SLOW(self, nums: List[int]) -> int:
        preSum = [0]
        n = len(nums)
        for num in nums:
            if num > 0:
                preSum.append(preSum[-1] + 1)
            else:
                preSum.append(preSum[-1] - 1)
        res = 0
        for i in range(1, n+1):
            for j in range(i):
                if preSum[i] - preSum[j] > 0:
                    res += 1
        return res


    def test(self):
        test_cases = [
            [0,0,0,1,1],
            [0,1,1,0,1],
            [0],
            [1],
            [1,1,1],
        ]
        for nums in test_cases:
            res1 = self.subarraysWithMoreZerosThanOnes(nums)
            res2 = self.subarraysWithMoreZerosThanOnes_SLOW(nums)
            print('res1: %s' % res1)
            print('res2: %s' % res2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
