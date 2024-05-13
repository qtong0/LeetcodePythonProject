from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_dia = 0
        for h, w in dimensions:
            if h*h + w*w > max_dia:
                max_area = h*w
                max_dia = max(max_dia, h*h + w*w)
            elif h*h + w*w == max_dia:
                max_area = max(max_area, h*w)
        return max_area

    def test(self):
        test_cases = [
            [[9,3],[8,6]],
            [[3,4],[4,3]],
            [[2,6],[5,1],[3,10],[8,4]],
        ]
        for dimensions in test_cases:
            res = self.areaOfMaxDiagonal(dimensions)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
