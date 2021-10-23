from typing import List


class Solution(object):
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        t, b = 0, 0
        for i in range(n):
            if tops[i] != tops[0]:
                t += 1
            if bottoms[i] != tops[0]:
                b += 1
            if i == n-1:
                return min(t, b)
            if tops[i] != tops[0] and bottoms[i] != tops[0]:
                break
        t, b = 0, 0
        for i in range(n):
            if tops[i] != bottoms[0]:
                t += 1
            if bottoms[i] != bottoms[0]:
                b += 1
            if i == n-1:
                return min(t, b)
            if tops[i] != bottoms[0] and bottoms[i] != bottoms[0]:
                break
        return -1

    def test(self):
        testCases = [
            [
                [2,1,2,4,2,2],
                [5,2,6,2,3,2],
            ],
            [
                [3,5,1,2,3],
                [3,6,3,3,4],
            ],
        ]
        for arrA, arrB in testCases:
            res = self.minDominoRotations(arrA, arrB)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
