class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        l, r = 0, 2**32-1
        while l <= r:
            mid = (l+r)//2
            if self.canSplit(sweetness, K, mid):
                l = mid + 1
            else:
                r = mid - 1
        return l-1

    def canSplit(self, nums, k, maxVal):
        splits, total = 0, 0
        for num in nums:
            if total + num < maxVal:
                total += num
            else:
                total = 0
                splits += 1
        return splits > k

    def test(self):
        testCases = [
            [[1,2,3,4,5,6,7,8,9], 5],
            [[5,6,7,8,9,1,2,3,4], 8],
            [[1,2,2,1,2,2,1,2,2], 2],
        ]
        for nums, k in testCases:
            res = self.maximizeSweetness(nums, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
