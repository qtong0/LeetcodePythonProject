from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        num = 0
        res = []
        for t in target:
            while num < t:
                res.append('Push')
                num += 1
                if num != t:
                    res.append('Pop')
        return res


    def test(self):
        test_cases = [
            [[1, 3], 3],
            [[1, 2, 3], 3],
            [[1, 2], 4],
            [[2, 3, 4], 4],
        ]
        for target, n in test_cases:
            res = self.buildArray(target, n)
            print('res: %s' % res)
            print('-='*30 + '-')


if __name__ == '__main__':
    Solution().test()
