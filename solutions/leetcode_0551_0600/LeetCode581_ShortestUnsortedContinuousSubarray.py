from typing import List


class Solution(object):
    # Instead of sorting, use O(N) solution like below
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        beg, end = -1, -2
        min_val, max_val = nums[n-1], nums[0]
        for i in range(1, n):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[n-1-i])
            if nums[i] < max_val:
                end = i
            if nums[n-1-i] > min_val:
                beg = n-1-i
        return end - beg + 1


    def findUnsortedSubarray_Sort(self, nums: List[int]) -> int:
        numsSorted = sorted(nums)
        i, j = 0, len(nums)-1
        while i < j and numsSorted[i] == nums[i]:
            i += 1
        if i == j:
            return 0
        while i < j and numsSorted[j] == nums[j]:
            j -= 1
        return j-i+1


    def test(self):
        testCases = [
            [2, 6, 4, 8, 10, 9, 15],
            [1, 2, 3, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findUnsortedSubarray(nums)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
