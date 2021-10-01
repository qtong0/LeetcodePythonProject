from typing import List
import math


class Solution:
    # Can-do binary search!
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, r = 1, 10**7
        res = -1
        while l <= r:
            mid = (l+r) // 2
            if self.canDo(mid, dist, hour):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res

    def canDo(self, speed, dist, hour):
        sumVal = 0
        for i, d in enumerate(dist):
            if i < len(dist)-1:
                sumVal += math.ceil(d / speed)
            else:
                sumVal += d / speed
        return sumVal <= hour

    def test(self):
        test_cases = [
            [[1,3,2], 6],
            [[1,3,2], 2.7],
            [[1,3,2], 1.9],
            [[1,1,100000], 2.01],
        ]
        for dist, hour in test_cases:
            res = self.minSpeedOnTime(dist, hour)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
