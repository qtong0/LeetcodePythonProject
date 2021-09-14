class Solution:
    """
    Explanation
    We have 4 plans:
        - kill 3 biggest elements
        - kill 2 biggest elements + 1 smallest elements
        - kill 1 biggest elements + 2 smallest elements
        - kill 3 smallest elements
    """

    def minDifference(self, nums: []) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float('inf')
        for i in range(4):
            res = min(res, nums[len(nums) - 4 + i] - nums[i])
        return res

    def test(self) -> None:
        testCases = [
            [5, 3, 2, 4],  # 0
            [1, 5, 0, 10, 14],  # 1
            [6, 6, 0, 1, 1, 4, 6],  # 2
            [1, 5, 6, 14, 15],  # 1
        ]
        for nums in testCases:
            res = self.minDifference(nums)
            print('res: %s' % res)
            print('-=' * 30 + '-')


if __name__ == '__main__':
    Solution().test()
