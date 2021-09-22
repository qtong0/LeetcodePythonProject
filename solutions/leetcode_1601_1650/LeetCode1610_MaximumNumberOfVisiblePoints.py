import math

class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        arr, extra = [], 0
        xx, yy = location
        for x, y in points:
            if xx == x and yy == y:
                extra += 1
            else:
                arr.append(math.atan2(y - yy, x - xx))

        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180

        l = res = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            res = max(res, r-l+1)

        return res + extra

    def test(self):
        test_cases = [
            [[[2,1],[2,2],[3,3]], 90, [1,1]],
            [[[2,1],[2,2],[3,4],[1,1]], 90, [1,1]],
            [[[1,0],[2,1]], 13, [1,1]],
        ]
        for points, angle, location in test_cases:
            res = self.visiblePoints(points, angle, location)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
