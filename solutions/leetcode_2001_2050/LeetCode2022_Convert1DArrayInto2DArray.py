from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        res = []
        curr = []
        for i, num in enumerate(original):
            curr.append(num)
            if i % n == n-1:
                res.append(curr)
                curr = []
        return res


    def test(self):
        test_cases = [
            [[1,2,3,4], 2, 2],
            [[1,2,3], 1, 3],
        ]
        for original, m, n in test_cases:
            res = self.construct2DArray(original, m, n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
