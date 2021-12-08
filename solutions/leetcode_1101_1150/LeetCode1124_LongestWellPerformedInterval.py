from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        arr = [1 if h > 8 else -1 for h in hours]
        sum_val = 0
        res = 0
        hashmap = {}
        for i, num in enumerate(arr):
            sum_val += num
            if sum_val > 0:
                res = i + 1
            if sum_val not in hashmap:
                hashmap[sum_val] = i
            if sum_val - 1 in hashmap:
                res = max(res, i-hashmap[sum_val-1])
        return res



    def test(self):
        test_cases = [
            [9,9,6,0,6,6,9],
            [9,6,9],
            [6,6,6],
            [6,6,9],
            [6,6,9,9],
        ]
        for hours in test_cases:
            res = self.longestWPI(hours)
            print('res: %s' % res)
            print('-='*30 + '-')



if __name__ == '__main__':
    Solution().test()
