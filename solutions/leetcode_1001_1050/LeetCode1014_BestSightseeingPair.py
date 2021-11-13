from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res, curr = 0, 0
        for val in values:
            res = max(res, curr + val)
            curr = max(curr, val) - 1
        return res


    def test(self):
        test_cases = [
            [3,7,2,3],
            [8,1,5,2,6],
            [1,2],
        ]
        for values in test_cases:
            res = self.maxScoreSightseeingPair(values)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
