from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        m, n = len(slots1), len(slots2)
        i, j = 0, 0
        while i < m and j < n:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []

    def test(self):
        test_cases = [
            [
                [[10,12],[15, 25]],
                [[0,100]],
                8,
            ],
            [
                [[10,60]],
                [[12,17],[21,50]],
                8,
            ],
            [[[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8],
            [[[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12],
        ]
        for slots1, slots2, duration in test_cases:
            res = self.minAvailableDuration(slots1, slots2, duration)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
