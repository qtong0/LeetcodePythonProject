from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)//2):
            t = nums[i*2]
            num = nums[i*2+1]
            res += [num]*t
        return res

    def test(self):
        test_cases = [
            [1,2,3,4],
            [1,1,2,3],
        ]
        for nums in test_cases:
            res = self.decompressRLElist(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
