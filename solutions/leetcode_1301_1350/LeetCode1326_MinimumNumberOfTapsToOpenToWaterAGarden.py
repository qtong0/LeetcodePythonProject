from typing import List


class Solution:
    # easier to understand
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0]*(n+1)
        for i, r in enumerate(ranges):
            if ranges[i] == 0:
                continue
            left = max(0, i-ranges[i])
            # arr[left] is max reach for [left, right]
            arr[left] = max(arr[left], i+ranges[i])

        res, max_reach, end = 0, 0, 0
        i = 0
        while i < len(arr) and end < n:
            res += 1
            while i < len(arr) and i <= end:
                max_reach = max(max_reach, arr[i])
                i += 1
            if end == max_reach:
                return -1
            end = max_reach
        return res

    # prev_end & end solution
    def minTaps_another(self, n: int, ranges: List[int]) -> int:
        arr = []
        for i, r in enumerate(ranges):
            arr.append([i-r, i+r])
        arr.sort(key=lambda a: [a[0], -a[1]])
        end, end2 = float('-inf'), 0
        res = 0
        for a in arr:
            if a[0] > end2:
                return -1
            if end < a[0] <= end2:
                res += 1
                end = end2
            if a[1] >= n:
                return res
            end2 = max(end2, a[1])
        return res if end2 >= n else -1


    def test(self):
        test_cases = [
            [5, [3,4,1,1,0,0]],
            [3, [0,0,0,0]],
            [7, [1,2,1,0,2,1,0,1]],
            [8, [4,0,0,0,4,0,0,0,4]],
            [68, [0,0,0,1,4,2,2,2,2,4,0,0,0,5,4,0,0,5,3,0,1,1,5,1,1,2,4,1,0,4,3,5,1,0,3,3,4,2,2,4,3,1,1,0,4,0,2,1,4,0,0,3,3,1,1,4,4,2,0,3,4,0,1,5,3,0,1,0,2]],
            [86, [1,2,1,3,2,0,0,5,5,5,0,1,3,4,3,0,1,2,1,4,5,3,1,3,2,1,0,5,4,3,1,1,4,2,0,5,1,5,2,0,1,0,4,4,4,0,2,2,4,5,0,2,3,2,0,2,2,3,3,2,0,5,3,0,5,3,1,3,3,2,5,2,4,4,4,5,4,1,1,0,3,1,4,3,1,3,1]],
        ]
        for n, ranges in test_cases:
            res = self.minTaps(n, ranges)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
