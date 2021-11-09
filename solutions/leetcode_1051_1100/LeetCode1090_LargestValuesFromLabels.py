from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        arr = sorted([(-v, i) for i, v in enumerate(values)])
        label_count = {}
        res = 0
        for v, i in arr:
            v = -v
            l = labels[i]
            if label_count.get(l, 0) < useLimit:
                res += v
                numWanted -= 1
                label_count[l] = label_count.get(l, 0) + 1
                if numWanted == 0:
                    return res
        return res

    def test(self):
        test_cases = [
            [[5,4,3,2,1], [1,1,2,2,3], 3, 1],
            [[5,4,3,2,1], [1,3,3,3,2], 3, 1],
            [[9,8,8,7,6], [0,0,0,1,1], 3, 1],
            [[9,8,8,7,6], [0,0,0,1,1], 3, 2],
        ]
        for values, labels, numWanted, useLimit in test_cases:
            res = self.largestValsFromLabels(values, labels, numWanted, useLimit)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
