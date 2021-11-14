from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = {}
        min_h, max_h = float('inf'), float('-inf')
        for h in heights:
            counter[h] = counter.get(h, 0) + 1
            min_h = min(min_h, h)
            max_h = max(max_h, h)
        res = 0
        i = 0
        for h in range(min_h, max_h+1):
            while counter.get(h, 0):
                res += heights[i] != h
                i += 1
                counter[h] -= 1
        return res


    def heightChecker_sort(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        res = 0
        for h1, h in zip(sorted_heights, heights):
            res += h1 != h
        return res


    def test(self):
        test_cases = [
            [1,1,4,2,1,3],
            [5,1,2,3,4],
            [1,2,3,4,5],
        ]
        for heights in test_cases:
            res_1 = self.heightChecker(heights)
            res_2 = self.heightChecker_sort(heights)
            print('res_1: %s' % res_1)
            print('res_2: %s' % res_2)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
