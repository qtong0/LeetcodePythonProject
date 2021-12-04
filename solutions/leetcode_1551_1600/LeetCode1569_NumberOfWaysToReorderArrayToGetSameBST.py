from typing import List
import math


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def ways_to_interleave(subsequence1, subsequence2):
            total_things = len(subsequence1) + len(subsequence2)
            things_to_choose = len(subsequence1)
            # math.comb(n, k) means how many combination choosing k from n
            # n! / (k! & (n-k)!)
            return math.comb(total_things, things_to_choose)

        def helper(subsequence):
            if not subsequence:
                return 1
            root_val = subsequence[0]
            left = [num for num in subsequence if num < root_val]
            right = [num for num in subsequence if num > root_val]
            ways_to_arrange_left = helper(left)
            ways_to_arrange_right = helper(right)
            return ways_to_arrange_left * ways_to_arrange_right * ways_to_interleave(left, right)

        return (helper(nums) - 1) % MOD


    def test(self):
        test_cases = [
            [3,4,5,1,2],
            [2,1,3],
            [1,2,3],
            [3,1,2,5,4,6],
            [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18],
        ]
        for nums in test_cases:
            res = self.numOfWays(nums)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
