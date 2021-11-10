from typing import List


class Solution(object):
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)
            stack.append(i)
        return res


    def test(self):
        testCases = [
            [0, 2, 0],
            [9, 0],
            [2,1,5,6,2,3],
            [2, 4],
            [10, 11, 12, 15],
        ]
        for heights in testCases:
            print('heights: %s' % (heights))
            result = self.largestRectangleArea(heights)
            print('result: %s' % (result))
            print('-='*15+'-')


if __name__ == '__main__':
    Solution().test()