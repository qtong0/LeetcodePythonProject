from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i + 1


    def longestOnes_Space(self, nums: List[int], k: int) -> int:
        queue = []
        res = 0
        left = -1
        for i, num in enumerate(nums):
            if num == 0:
                queue.append(i)
                res = max(res, i-left-1)  # Check this first
                if len(queue) > k:
                    left = queue.pop(0)
        res = max(res, len(nums)-left-1)
        return res


    def test(self):
        testCases = [
            [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3],
            [[1,1,1,0,0,0,1,1,1,1,0], 2],
            [[0,0,1,1,1,0,0], 0],
            [[1,1,1,1], 0],
            [[0,0,1,1,1,0,0,1,1,1,1], 0],
            [[0,0,0,1], 4],
            [[0,0,0,1], 2],
            [[1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8],
        ]
        for arr, k in testCases:
            res = self.longestOnes(arr, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
