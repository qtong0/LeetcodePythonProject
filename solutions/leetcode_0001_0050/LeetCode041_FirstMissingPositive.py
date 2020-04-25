class Solution(object):
    def firstMissingPositive(self, nums) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1
        for i in range(n):
            idx = abs(nums[i])
            if idx <= n:
                idx -= 1
                if nums[idx] > 0:
                    nums[idx] = -1 * nums[idx]
        for i in range(1, n):
            if nums[i] >= 0:
                return i+1
        return n+1

    def test(self):
        testCases = [
            [1,2,0],
            [3,4,-1,1],
            [7,8,9,11,12],
        ]
        for nums in testCases:
            res = self.firstMissingPositive(nums)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
