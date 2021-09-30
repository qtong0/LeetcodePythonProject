from typing import List


class Solution:
    # Two pointers
    def maximumScore(self, nums: List[int], k: int) -> int:
        i, j = k, k
        n = len(nums)
        res, minVal = nums[k], nums[k]
        while 0 < i or j < n-1:
            if i == 0:
                j += 1
            elif j == n-1:
                i -= 1
            elif nums[i-1] < nums[j+1]:
                j += 1
            else:
                i -= 1
            minVal = min(minVal, nums[i], nums[j])
            res = max(res, minVal * (j-i+1))
        return res

    # O(N*N) is not good enough :(
    def maximumScore_own_TLE(self, nums: List[int], k: int) -> int:
        res = float('-inf')
        n = len(nums)
        minVals = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            minVal = float('inf')
            for j in range(i, -1, -1):
                minVal = min(minVal, nums[j])
                minVals[j][i] = minVal
        for i in range(k, -1, -1):
            for j in range(k, len(nums)):
                res = max(res, (minVals[i][j]) * (j - i + 1))
        return res

    def test(self):
        test_cases = [
            [[1,4,3,7,4,5], 3],
            [[5,5,4,5,4,1,1,1], 0],
        ]
        for nums, k in test_cases:
            res = self.maximumScore(nums, k)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
