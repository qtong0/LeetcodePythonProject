from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            div_sum = self.getDivisionSum(nums, mid)
            if div_sum <= threshold:
                r = mid
            else:
                l = mid+1
        return l

    def getDivisionSum(self, nums, divider):
        res = 0
        for num in nums:
            if num % divider == 0:
                res += num // divider
            else:
                res += num // divider + 1
        return res

    def test(self):
        test_cases = [
            [[1,2,5,9], 6],
            [[44,22,33,11,1], 5],
            [[21212,10101,12121], 1000000],
            [[2,3,5,7,11], 11],
        ]
        for nums, threshold in test_cases:
            res = self.smallestDivisor(nums, threshold)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
