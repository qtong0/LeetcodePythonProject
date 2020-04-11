class Solution(object):
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        cur_sum = max_sum = nums[0]
        for i in range(1, n):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def test(self):
        testCases = [
            [-2,1,-3,4,-1,2,1,-5,4],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maxSubArray(nums)
            print('result: %s' % (result))
            print('-='*15+'-')


if __name__ == '__main__':
    Solution().test()
