from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res


    def test(self):
        test_cases = [
            [10,6,8,5,11,9],
            [5,1,2,3,10],
        ]
        for heights in test_cases:
            res = self.canSeePersonsCount(heights)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
