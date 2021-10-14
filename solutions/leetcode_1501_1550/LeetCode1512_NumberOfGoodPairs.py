from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0
        for num in nums:
            if num in hashmap:
                res += hashmap[num]
            hashmap[num] = hashmap.get(num, 0) + 1
        return res

    def test(self):
        test_cases = [
            [1,2,3,1,1,3],
            [1,1,1,1],
            [1,2,3],
        ]
        for nums in test_cases:
            res = self.numIdenticalPairs(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
