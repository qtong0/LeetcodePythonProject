from typing import List
import math

class Solution(object):
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        count, n = 0, len(stations)
        left, right = 0, stations[-1]-stations[0]
        while left + 1e-6 < right:
            mid = (left+right)/2.0
            count = 0
            for i in range(n-1):
                count += math.ceil((stations[i+1]-stations[i])/mid)-1
            if count > k:
                left = mid
            else:
                right = mid
        return right


    def test(self):
        testCases = [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                9,
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                7,
            ],
        ]
        for stations, k in testCases:
            print('stations: %s' % stations)
            print('K: %s' % k)
            result = self.minmaxGasDist(stations, k)
            print('result: %s' % result)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
