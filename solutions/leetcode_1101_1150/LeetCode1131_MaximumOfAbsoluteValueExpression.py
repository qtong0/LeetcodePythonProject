from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res, n = 0, len(arr1)
        for p, q in (1, 1), (1, -1), (-1, 1), (-1, -1):
            smallest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                curr = p * arr1[i] + q * arr2[i] + i
                res = max(res, curr - smallest)
                smallest = min(smallest, curr)
        return res

    def test(self):
        test_cases = [
            [[1,2,3,4], [-1,4,5,6]],
            [[1,-2,-5,0,10], [0,-2,-1,-7,-4]],
        ]
        for arr1, arr2 in test_cases:
            res = self.maxAbsValExpr(arr1, arr2)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
