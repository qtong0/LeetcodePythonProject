from typing import List


class Solution(object):
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        res = 0
        maxLen = 0
        lengths = [0]*n
        counts = [0]*n
        for i in range(n):
            lengths[i], counts[i] = 1, 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] == lengths[j]+1:
                        counts[i] += counts[j]
                    elif lengths[i] < lengths[j]+1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
            if maxLen == lengths[i]:
                res += counts[i]
            elif maxLen < lengths[i]:
                maxLen = lengths[i]
                res = counts[i]
        return res



    def test(self):
        testCases = [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
            [1, 2, 4, 3, 5, 4, 7, 2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findNumberOfLIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')



if __name__ == '__main__':
    Solution().test()
