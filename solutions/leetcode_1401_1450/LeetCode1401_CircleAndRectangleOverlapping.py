class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        if x1 <= x_center + radius and x2 >= x_center - radius and y1 <= y_center <= y2:
            return True
        if x2 >= x_center - radius and x1 <= x_center + radius and y1 <= y_center <= y2:
            return True
        if y1 <= y_center + radius and y2 >= y_center - radius and x1 <= x_center < x2:
            return True
        if y2 >= y_center - radius and y1 <= y_center + radius and x1 <= x_center < x2:
            return True
        if (x1 - x_center)**2 + (y1 - y_center)**2 <= radius**2:
            return True
        if (x1 - x_center)**2 + (y2 - y_center)**2 <= radius**2:
            return True
        if (x2 - x_center)**2 + (y1 - y_center)**2 <= radius**2:
            return True
        if (x2 - x_center)**2 + (y2 - y_center)**2 <= radius**2:
            return True
        return False

    def test(self):
        test_cases = [
            [1, 0, 0, 1, -1, 3, 1],
            [1, 0, 0, -1, 0, 0, 1],
            [1, 1, 1, -3, -3, 3, 3],
            [1, 1, 1, 1, -3, 2, -1],
            [24, 13, 1, 0, 15, 5, 18],
        ]
        for radius, x_center, y_center, x1, y1, x2, y2 in test_cases:
            res = self.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
