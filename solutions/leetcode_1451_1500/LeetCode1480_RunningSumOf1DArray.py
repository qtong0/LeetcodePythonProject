from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]
        for num in nums:
            res.append(res[-1]+num)
        return res[1:]

    def test(self):
        test_cases = [
            [1,2,3,4],
            [1,1,1,1,1],
            [3,1,2,10,1],
        ]
        for nums in test_cases:
            res = self.runningSum(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
